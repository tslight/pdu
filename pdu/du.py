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
    for entry in os.scandir(path):
        try:
            is_dir = entry.is_dir(follow_symlinks=False)
        except:
            err = "!"
            break
        if is_dir:
            total += calc(entry.path)[0]
        else:
            try:
                total += entry.stat(follow_symlinks=False).st_size
            except:
                err = "!"
                break
    return total, err


def du(path):
    '''
    Put it all together!
    '''
    size, err = calc(path)
    if err:
        return err
    hr, unit = convert(size)
    hr = str(hr)
    result = hr + " " + unit
    return result
