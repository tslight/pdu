# Copyright (c) 2018, Toby Slight. All rights reserved.
# ISC License (ISCL) - see LICENSE file for details.

import os


def convert(b):
    '''
    takes a number of bytes as an argument and returns the most suitable human
    readable unit conversion.
    '''
    if b > 1024**3:
        hr = round(b/1024**3)
        unit = "GB"
    elif b > 1024**2:
        hr = round(b/1024**2)
        unit = "MB"
    else:
        hr = round(b/1024)
        unit = "KB"
    return hr, unit


def calc(path):
    '''
    Takes a path as an argument and returns the total size in bytes of the file
    or directory. If the path is a directory the size will be calculated
    recursively.
    '''
    total = 0
    err = None
    if os.path.isdir(path):
        try:
            for entry in os.scandir(path):
                try:
                    is_dir = entry.is_dir(follow_symlinks=False)
                except (PermissionError, FileNotFoundError):
                    err = "!"
                    return total, err
                if is_dir:
                    result = calc(entry.path)
                    total += result[0]
                    err = result[1]
                    if err:
                        return total, err
                else:
                    try:
                        total += entry.stat(follow_symlinks=False).st_size
                    except (PermissionError, FileNotFoundError):
                        err = "!"
                        return total, err
        except (PermissionError, FileNotFoundError):
            err = "!"
            return total, err
    else:
        total += os.path.getsize(path)
    return total, err


def du(path):
    '''
    Put it all together!
    '''
    size, err = calc(path)
    if err:
        return err
    else:
        hr, unit = convert(size)
        hr = str(hr)
        result = hr + " " + unit
        return result
