#! python3

import pyperclip
import sys
import webbrowser

url = 'www.baidu.com'
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get Address from clipboard.
    address = pyperclip.paste()

webbrowser.open(url)


