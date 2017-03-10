#! python3

import re


def strip(source, replace):
    if replace is None:
        stripRegex = re.compile(r'''(^\w+)(\w+$)''')
    else:
        stripRegex = re.compile(r'''(replace)''')
    return stripRegex.sub("", source)
