#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import csv


def test_csv_read():
    exampleFile = open('example.csv')
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
    print(exampleData)
    print(exampleData[0][0])

    for row in exampleData:
        print('Row #' + str(exampleReader.line_num) + ' ' + str(row))


def test_csv_write():
    with open('output.csv', 'w', newline='') as outputFile:
        outputwriter = csv.writer(outputFile)
        outputwriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
        outputwriter.writerow(['Hello, world', 'eggs', 'bacon', 'ham'])
        outputwriter.writerow([1, 2, 3.141592, 4])


if __name__ == '__main__':
    test_csv_write()