#!/usr/bin/env python3

import os

def run():
    print('[*] In listdir module')
    files = os.listdir('.')
    return str(files)