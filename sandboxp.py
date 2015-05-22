#!/usr/bin/env python3

import os, sys


sys.meta_path = [GitImport()]

def detect():
    max_keystrokes = 25
    max_mouse_clicks = 25

    double_clicks = 0
    max_double_clicks = 10
    double_click_threshold = .4
    first_double_click = None

    average_mousetime = 0
    max_input_threshold = 30 * 1000 # ms

    previous_timestamp = None
    detection_complete = False

    # last_input = idle.run()
