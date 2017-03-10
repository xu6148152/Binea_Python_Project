  spam = ['apples', 'bananas', 'tofu', 'cats']


def convert(list):
    result = ''
    for index in range(len(spam) - 1):
        result += spam[index] + ","
    result += 'and ' + spam[len(spam) - 1]
    return result

if __name__ == '__main__':
    result = convert(spam)
    print(result)
