#! python3

import re

textReg = re.compile(r'''(
    ([a-zA-Z]){7,}(\d+)
)
''', re.VERBOSE)


def checkText(text):
    result = textReg.search(text)
    if result is None:
        return False
    else:
        return True


if __name__ == '__main__':
    text = "aaaaaaaaa1"
    print(checkText(text))
