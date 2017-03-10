import os
import re
import originSqlRefine
import sys

import myUtil

def main(path):
    
    # myUtil.myPopen(myUtil.svnCmd + ' up', path, encoding='gbk')
    
    outpath = r'./sql//'

    if not os.path.isdir(outpath):
        os.mkdir(outpath)



    for i in os.listdir(path):
        if i.endswith(".sql") :
            i = i.lower()
            print(i)
            tablename = i.replace(".sql", '')
            print('tablename=' + tablename)
            with open(path + i, 'r') as f:
                sqls = f.read().split(';')
                print( sqls[0])

                fout = open(outpath + i, 'w')
                print('fout=' + outpath + i)
                for sql in sqls:
                    sql = sql.strip()
                    if (sql.startswith('BEGIN') or sql.startswith('COMMIT') or len(sql) == 0):
                        continue


                    m = re.findall(r'\".+?\"',sql)

                    for word in m:

                        wordnew = word[1:-1]

                        sql = sql.replace(word, wordnew)



                    m = re.findall(r'\`.+?\`',sql)

                    for word in m:

                        wordnew = word[1:-1]

                        sql = sql.replace(word, wordnew)



                    sql = sql.replace('\n', ' ')
                    sql = sql.replace('UNIQUE', ' ')

#                     if (tablename == 'clubs') :
#                         print (sql)

                    
                    #change table name to lower case
                    
                    if tablename in sql.lower():
                        print('sub:'+tablename)
                        sql = re.sub(tablename, tablename.lower(), sql,  flags=re.IGNORECASE)
                    
                    sql = sql.replace('Club_Information', 'Club_Information'.lower())
                    
                    if sql.startswith('INSERT INTO club_information'):
                        index = sql.find('VALUE')
                        sql = sql[:index] + ' (Make_ID ,      Model_ID ,      Make_Name,      Model_Name ,      Type_1,      Type_2 ,      Loft ,      Length  ,      Shaft ,      Flex ,      icon_index ) '+sql[index:]
                        
                    
                    
                    fout.write(sql + ';\n')
                fout.close()

    print('====end of main')


if __name__ == '__main__':
    path = ''
    if len(sys.argv) > 1:
        path = r'/Users/zeppmac/Dropbox/golfsense/python/sql/ios/'
    else:
        path = r'/Users/zeppmac/Dropbox/golfsense/python/sql/ios/'
        # raise Exception('Please input ios svn root path')
#         path =  r'd:\workspace\golfsense\svn_gs2\ios\golfsense\trunk\model\db_p\tablemodel\\'
        
    
    main(path)
    originSqlRefine.main()
