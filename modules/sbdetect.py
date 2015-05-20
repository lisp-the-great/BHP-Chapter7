#!/usr/bin/env python3

import sys
import time
import ctypes
import random


user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

keystrokes = 0
mouseclicks = 0
doubleclicks = 0

