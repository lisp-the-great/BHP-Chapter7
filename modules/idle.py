#!/usr/bin/env python3

import os, sys


def run():
    """Check the idle time
        :return idle-time in ms <float>
    """
    if os.name == 'nt':
        import ctypes
        user32 = ctypes.windll.user32
        kernel32 = ctypes.windll.kernel32
        class LastInputInfo(ctypes.Structure):
            _fields_ = [
                ('cbSize', ctypes.c_uint),
                ('dwTime', ctypes.c_ulong)
            ]
        _info = LastInputInfo()
        _info.cbSize = ctypes.sizeof(LastInputInfo)
        user32.GetLastInputInfo(ctypes.byref(__info))
        uptime = kernel32.GetTickCount()
        return uptime - _info.dwTime
    elif sys.platform == 'darwin':
        import subprocess as subp
        command = ("/usr/sbin/ioreg -c IOHIDSystem | /usr/bin/awk "
                   "'/HIDIdleTime/ { print $NF/1000000000; exit }'")
        output = subp.check_output(command, stderr=subp.STDOUT, shell=True)
        return float(output.strip())
    elif sys.platform == 'linux':
        pass
    else:
        pass
