#!/usr/bin/env python3


import os, sys
import time


def run():
    event = { 'mouse': 0, 'double': 0, 'key': 0, 'time': 0 }
    if os.name == 'nt':
        import ctypes
        user32 = ctypes.windll.user32
        kernel32 = ctypes.windll.kernel32
        for i in range(0xff):
            if user32.GetAsyncKeyState(i) == -0x7fff:
                if i == 0x1:
                    event['mouse'] += 1
                    event['time'] = time.time()
                    return event
                elif 32 < i < 127:
                    event['key'] += 1
        return None
