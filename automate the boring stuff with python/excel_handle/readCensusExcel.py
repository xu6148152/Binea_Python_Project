#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import openpyxl
import pprint
import os

if not os.path.exists('census2010.py'):
    print('Opening workbook...')
    wb = openpyxl.load_workbook('censuspopdata.xlsx')
    sheet = wb.get_sheet_by_name('Population by Census Tract')
    countyData = {}

    # TODO Fill in countyData with each county's population and tracts
    print('Reading rows...')
    for row in range(2, sheet.max_row + 1):
        # Each row in the the spreadsheet has data for one census tract.
        state = sheet['B' + str(row)].value
        county = sheet['C' + str(row)].value
        pop = sheet['D' + str(row)].value

        # Make sure the key for this state exists.
        countyData.setdefault(state, {})

        # Make sure the key for this county in this state exists
        countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

        # Each row represents one census tract, so increment by once
        countyData[state][county]['tracts'] += 1

        # Increase the county pop by the pop in this census tract.
        countyData[state][county]['pop'] += int(pop)

    # TODO Open a new text file and write the contents of countyData to it
    print('Writing results...')
    with open('census2010.py', 'w') as resultFile:
        resultFile.write('allData = ' + pprint.pformat(countyData))
else:
    from excel_handle import census2010
    anchoragePop = census2010.allData['AK']['Anchorage']['pop']
    print('The 2010 population of Anchorage was ' + str(anchoragePop))
