from __future__ import print_function

import sys
import os
import re

def getColumnNameAndType(s):
    d = ''
    index = 0



    index2 = s.find(' ', index+1 )

    s2 = s[index2 + 1:].strip()
    index3 = s2.find(' ')



    n = s[index:index2]
    t  = s2[:index3]

    index_default = s.find('DEFAULT' ) + 7
    d = s[index_default:].strip()
    if d=="''":
        d='""'
    return n, t, d

def hasNoAlpha(s):
    return re.search('[a-zA-Z]', s)   is None

def iter_islast(iterable):
    """ iter_islast(iterable) -> generates (item, islast) pairs

Generates pairs where the first element is an item from the iterable
source and the second element is a boolean flag indicating if it is the
last item in the sequence.
"""

    it = iter(iterable)
    prev = next(it)
    for item in it:
        yield prev, False
        prev = item
    yield prev, True


def main():
    
    path =  r"./sql/"

    outfile = open(path+"DataStructs.java", 'w')
    outfile.write('''package com.zepp.golfsense.data.models;


import android.net.Uri;
import android.provider.BaseColumns;


public class DataStructs {

	public static final String AUTHORITY = "com.zepp.golfsense.data.models.DataStructs";
	public static final String CONTENT_TYPE = "vnd.android.cursor.dir/vnd.zepp.golfsense";
	public static final String CONTENT_ITEM_TYPE = "vnd.android.cursor.item/vnd.zepp.golfsense";

	// this class cannot be instantiatized
	private DataStructs() {
	}
''')


    

    bean = ''

    for i in os.listdir(path):
        if i.endswith(".sql") and not i.startswith("prodata") and not i.startswith('club_information_update_2') \
        and not i.startswith('swing_video.sql') :
            print('begin process ' + i)
            tablename = i.replace(".sql", "")

            outfile.write('\n/* Table name: '+tablename+' */\n')

            outfile.write('public static final class ' + tablename[0].upper() + tablename[1:]+'Columns implements BaseColumns {\n')
            outfile.write('public static final String TABLE_NAME = "' + tablename + '";\n')

            outfile.write('''public static final String CONTENT_BOX = "content://" + AUTHORITY + "/"
    				+ TABLE_NAME;
    		public static final Uri CONTENT_URI = Uri.parse(CONTENT_BOX);
    		public static final String CONTENT_TYPE = "vnd.android.cursor.dir/vnd.zepp.golfsense."
    				+ TABLE_NAME;
    		public static final String CONTENT_ITEM_TYPE = "vnd.android.cursor.item/vnd.zepp.golfsense."
    				+ TABLE_NAME;\n''')

            beanname =  'ZG' +  tablename[0].upper() + tablename[1:] + 'Bean'
            f2 = open(path + beanname+'.java', 'w')
            print('bean file name='+path + beanname+'.java')
            bean = '''package com.zepp.golfsense.data.models;

    import java.io.Serializable;
    import android.content.ContentValues;

    import com.zepp.golfsense.data.models.DataStructs.''' + tablename[0].upper() + tablename[1:] + '''Columns;

    public class ZG''' + tablename[0].upper() + tablename[1:] + '''Bean implements Serializable, ZGBean {

    	private static final String TAG = ZG''' + tablename[0].upper() + tablename[1:] + '''Bean.class.getSimpleName();\n'''


            beanconstruct = '''public ZG''' + tablename[0].upper() + tablename[1:] + '''Bean() {\n'''
            beancopyconstruct = 'public ZG' + tablename[0].upper() + tablename[1:] + 'Bean(ZG' + \
                tablename[0].upper() + tablename[1:] +'''Bean copy) {\n'''

            beanToContentValue = '''@Override
	public ContentValues toContentValues() {
		ContentValues cv = new ContentValues();\n'''

            beanFromContentValue = '''@Override
	public ZG'''+ tablename[0].upper() + tablename[1:] +'''Bean fromContentValues(ContentValues cv) {\n'''

            projection = '''public static final String[] PROJECTION = new String[] {_ID'''
            with open(path + i, 'r') as f:
                is_first = True

                createSql = f.readline()
                columnsAndTypesStr = re.search(r'\((.+)\)', createSql).group(1)

                print('columns=\n')
                print(columnsAndTypesStr)

                columnsList = re.split(r',(?![0-9])',columnsAndTypesStr)
                print('len=' +str(len(columnsList)))
                [print('item=' + i) for i in columnsList]





                totalcolumns = ''
                for columnAndType in columnsList:
                    columnAndType = columnAndType.strip()

                    column, ty, defaultValue = getColumnNameAndType(columnAndType)
                    column = column.strip()
                    print("column = " + column + '\n type = <<' + ty + '>>')

                    totalcolumns += column + ','

                    beancolumn = 'private '
                    typename = ''

                    if  ty.startswith('timestamp')  or ty.startswith('bigint') or column == "device_swing_time" or column == "group_id":
                        typename = 'long '
                        typename1 = 'Long'

                        beanconstructcolumn = column + ' = '+ defaultValue + ';\n'
                    elif ty.startswith('TEXT') or ty.startswith('varchar'):
                        typename = 'String '
                        typename1 = 'String'

                        beanconstructcolumn = column + ' = ' + defaultValue +';\n'
                    elif ty.startswith('REAL') or ty.startswith('decimal'):
                        typename = 'double '
                        typename1 = 'Double'
                        beanconstructcolumn = column + ' = ' + defaultValue + ';\n'
                    elif ty.startswith('INTEGER') or ty.startswith('int') or ty.startswith('tinyint'):
                        typename = 'int '
                        typename1 = 'Integer'

                        beanconstructcolumn = column + ' = '+ defaultValue + ';\n'
                    elif  ty.startswith('bigint'):
                        typename = 'long '
                        typename1 = 'Long'

                        beanconstructcolumn = column + ' = '+ defaultValue + ';\n'
                        
                    else:
                        raise ValueError

                    beancolumn = beancolumn + typename + column + ';\n'


                    beancopyconstructcolumn = column + ' = copy.' + column + ';\n'


                    outfile.write('public static final String ' + column.upper() + ' = "' + column + '";\n')

                    if not is_first:
                        bean = bean + beancolumn
                        beanconstruct = beanconstruct + beanconstructcolumn
                        beancopyconstruct = beancopyconstruct + beancopyconstructcolumn
                        beanToContentValue = beanToContentValue + 'cv.put(' + tablename[0].upper() + tablename[1:]+'Columns.' + column.upper() + ', ' + column + ');\n'
                        #id = cv.getAsString("id");

                        beanFromContentValue = beanFromContentValue + column +' = cv.getAs'+ typename1 + '(' +  tablename[0].upper() + tablename[1:]+'Columns.' + column.upper() + ');\n'
                        projection = projection + ', ' +  column.upper()
                    else:
                        is_first = False
                
                print ('file=' + i + ' total columns=' + totalcolumns)


            beanconstruct = beanconstruct + '}\n\n'
            beancopyconstruct = beancopyconstruct + '}\n\n'
            beanToContentValue = beanToContentValue + 'return cv;\n}\n\n'
            beanFromContentValue = beanFromContentValue + 'return this;\n}\n\n'

            bean = bean + beanconstruct + beancopyconstruct + beanToContentValue + beanFromContentValue +  '}\n\n'

            f2.write(bean)
            f2.close()

            outfile.write('''public static final String DEFAULT_SORT_ORDER = "_id asc";\n''')
            outfile.write(projection + ' };\n\n}\n\n')



    outfile.write('}\n\n')

    outfile.close()



if __name__ == '__main__':
    main()