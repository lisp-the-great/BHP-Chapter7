#!/usr/bin/env python3

import os

def run(**kwargs):
    print('[*] In listdir module.')
    files = os.listdir('.')
    return str(files)