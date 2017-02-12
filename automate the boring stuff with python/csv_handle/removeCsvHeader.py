#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue
    print('Removing header from ' + csvFilename + '...')

    # Read the csv file in (skipping first row).
    csvRows = []
    with open(csvFilename) as csvFileObj:
        readerObj = csv.reader(csvFileObj)
        for row in readerObj:
            if readerObj.line_num == 1:
                continue
            csvRows.append(row)

    # Write out the csv file
    with open(os.path.join('headerRemoved', csvFilename), 'w', newline='') as csvFileObj:
        csvWriter = csv.writer(csvFileObj)
        for row in csvRows:
            csvWriter.writerow(row)
