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
    if os.path.isdir(path):
        for entry in os.scandir(path):
            try:
                if entry.is_dir(follow_symlinks=False):
                    total += calc(entry.path)[0]
                else:
                    total += entry.stat(follow_symlinks=False).st_size
            except:
                return "!"
    else:
        total += os.path.getsize(path)
    return total


def du(path):
    '''
    Put it all together!
    '''
    size = calc(path)
    if isinstance(size, int):
        hr, unit = convert(size)
        hr = str(hr)
        result = hr + " " + unit
        return result
    return "!"
