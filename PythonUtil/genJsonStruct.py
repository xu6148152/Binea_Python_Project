import collections
import os
import shutil

import json


longKeys = ['client_id', 'user_id', 'group_id', 'client_created', 'device_created']
listKeys =[]

def main():
    s='''
   {"user_info":{"id":213716,"uuid":"7c25c9c0-b194-41c3-a56b-bfc27885627a","email":"096@a.aa","role":2,"created_at":"2014-11-24T06:11:35.000Z","updated_at":"2014-11-24T07:58:45.435Z","first_name":"096","last_name":"5","handicap_style":0,"handicap_style_1":0,"handicap_style_2":0,"height":"160.02","birth_year":1904,"gender":0,"right_handed":0,"grip_posture":"3.0","grip_position":"10.0","is_phone_timer":1,"video_record":1,"auto_save":1,"auto_comment":1,"sound_effect":1,"text_hint":1,"power_save":0,"unit":0,"impact_detect":1,"goals":"2|0|1,3.000:2,270.000:3,0.000:4,0.000:5,85.000:6,78.000:7,72.000:8,70.000:9,65.000:10,0.000:11,0.000","user_image_file_name":null,"user_image_content_type":null,"user_image_file_size":null,"user_image_fingerprint":"","versions":null,"language":"zh","timezone":8,"test_account":false,"flags":2,"extra":{"golf_ready_to_swing":1,"baseball_ready_to_swing":0}},"avatar_url":"","golf_clubs":[{"id":3242831,"user_id":213716,"type1":4,"type2":1,"shaft1":1,"shaft2":0,"length":"100.33","posture":1,"position":1,"face_angle":1,"maker_id":0,"model_id":13,"set_id":1,"created_at":"2014-11-24T06:18:55.000Z","updated_at":"2014-11-24T06:18:55.000Z"},{"id":3242832,"user_id":213716,"type1":4,"type2":2,"shaft1":1,"shaft2":0,"length":"99.06","posture":1,"position":1,"face_angle":2,"maker_id":0,"model_id":13,"set_id":1,"created_at":"2014-11-24T06:18:55.000Z","updated_at":"2014-11-24T06:18:55.000Z"},{"id":3242833,"user_id":213716,"type1":4,"type2":3,"shaft1":1,"shaft2":0,"length":"97.79","posture":1,"position":1,"face_angle":2,"maker_id":0,"model_id":13,"set_id":1,"created_at":"2014-11-24T06:18:55.000Z","updated_at":"2014-11-24T06:18:55.000Z"},{"id":3242834,"user_id":213716,"type1":4,"type2":4,"shaft1":1,"shaft2":0,"length":"96.52","posture":1,"position":1,"face_angle":2,"maker_id":0,"model_id":13,"set_id":1,"created_at":"2014-11-24T06:18:55.000Z","updated_at":"2014-11-24T06:18:55.000Z"},{"id":3242835,"user_id":213716,"type1":4,"type2":5,"shaft1":1,"shaft2":0,"length":"95.25","posture":1,"position":1,"face_angle":2,"maker_id":0,"model_id":13,"set_id":1,"created_at":"2014-11-24T06:18:55.000Z","updated_at":"2014-11-24T06:18:55.000Z"},{"id":3242836,"user_id":213716,"type1":4,"type2":6,"shaft1":1,"shaft2":0,"length":"93.98","posture":1,"position":1,"face_angle":2,"maker_id":0,"model_id":13,"set_id":1,"created_at":"2014-11-24T06:18:55.000Z","updated_at":"2014-11-24T06:18:55.000Z"},{"id":3242837,"user_id":213716,"type1":4,"type2":7,"shaft1":1,"shaft2":0,"length":"92.71","posture":1,"position":1,"face_angle":2,"maker_id":0,"model_id":13,"set_id":1,"created_at":"2014-11-24T06:18:55.000Z","updated_at":"2014-11-24T06:18:55.000Z"},{"id":3242838,"user_id":213716,"type1":4,"type2":8,"shaft1":1,"shaft2":0,"length":"91.44","posture":1,"position":1,"face_angle":2,"maker_id":0,"model_id":13,"set_id":1,"created_at":"2014-11-24T06:18:55.000Z","updated_at":"2014-11-24T06:18:55.000Z"},{"id":3242839,"user_id":213716,"type1":5,"type2":1,"shaft1":1,"shaft2":0,"length":"90.17","posture":1,"position":1,"face_angle":2,"maker_id":0,"model_id":13,"set_id":1,"created_at":"2014-11-24T06:18:55.000Z","updated_at":"2014-11-24T06:18:55.000Z"},{"id":3242840,"user_id":213716,"type1":5,"type2":3,"shaft1":1,"shaft2":0,"length":"88.9","posture":1,"position":1,"face_angle":2,"maker_id":0,"model_id":13,"set_id":1,"created_at":"2014-11-24T06:18:55.000Z","updated_at":"2014-11-24T06:18:55.000Z"}],"status":200}

'''
    jsonDict = json.loads(s)



    out = 'public class jsonDict{\n'
    print('json dict = '+str(jsonDict))
    print(str(type(int)), str(type(0)))
    print((type(1))== (type(0)))

    
    
    with open('jsonStruct.java', 'w') as f:
        f.write( getGsonString(jsonDict))

    for _ in set(listKeys):
        print('public static final String '+_+' = "'+_+'";')


def getGsonString(jsonDict={}, className=None):
     

    out = ''

    if className != None:
        out+='public static class ' + className + ' {\n'

    for jsonKey in collections.OrderedDict(sorted(jsonDict.items())):
        print(str(type(jsonKey)) +'=========' + str(jsonKey) +'====' +str(type(jsonDict[jsonKey])) + '==='+str( jsonDict[jsonKey]) + '\n')
        if(type(jsonKey) == type('')):
            listKeys.append(jsonKey)
            
        if mytype(jsonDict[jsonKey]) == type(0):
            print('type is int')
            if jsonKey == 'id' or jsonKey in longKeys:
                out += 'long '+ jsonKey + ';//' + str(jsonDict[jsonKey]) +'\n'
                out += genGetFunc('long', jsonKey)
            else:
                out += 'int '+ jsonKey + ';//' + str(jsonDict[jsonKey]) +'\n'
                out += genGetFunc('int', jsonKey)
        elif mytype(jsonDict[jsonKey]) == type(''):
            print('type is str')
            out += 'String '+ jsonKey + ';//' + str(jsonDict[jsonKey]) +'\n'
            out +=  genGetFunc('String', jsonKey)
        elif mytype(jsonDict[jsonKey]) == type(0.0):
            print('type is double')
            out += 'double '+ jsonKey + ';//' + str(jsonDict[jsonKey]) +'\n'
            out +=  genGetFunc('double', jsonKey)
        elif mytype(jsonDict[jsonKey]) == type(False):
            print('type is bool')
            out += 'boolean '+ jsonKey + ';//' + str(jsonDict[jsonKey]) +'\n'
            out +=  genGetFunc('boolean', jsonKey)

        elif mytype(jsonDict[jsonKey]) == type([]):
            print('type is array')
            try:
                
                out += getFirstCapital(jsonKey) + '[] ' + jsonKey + '; \n'
                out +=  genGetFunc(getFirstCapital(jsonKey) + '[]', jsonKey)
                print('jsonDict=' +str( jsonDict))
                print('jsonKey=' + jsonKey)
                classDef = getGsonString(jsonDict[jsonKey][0], getFirstCapital(jsonKey))
                out += classDef
            except TypeError  as e:
                if mytype(jsonDict[jsonKey][0]) == type(0):
                    print('type is int array')    
                    if jsonKey == 'id' or jsonKey in longKeys:
                        out += 'long [] '+ jsonKey + ';\n'
                        out += genGetFunc('long []', jsonKey)
                    else:
                        out += 'int []'+ jsonKey + ';\n'
                        out += genGetFunc('int []', jsonKey)
                        
                elif mytype(jsonDict[jsonKey]) == type(''):
                    print('type is str')
                    out += 'String [] '+ jsonKey + ';\n'
                    out +=  genGetFunc('String []', jsonKey)
                elif mytype(jsonDict[jsonKey]) == type(0.0):
                    print('type is double')
                    out += 'double []'+ jsonKey + ';\n'
                    out +=  genGetFunc('double[]', jsonKey)
                elif mytype(jsonDict[jsonKey]) == type(False):
                    print('type is bool')
                    out += 'boolean []'+ jsonKey + ';\n'
                    out +=  genGetFunc('boolean []', jsonKey)
            except IndexError as e1:
                print('IndexError e1=' + e1)
                pass    
                
                
                
                
                
                
                
                
                
                
        elif mytype(jsonDict[jsonKey]) == type({}):
            print('type is dict')
            out += getFirstCapital(jsonKey) + ' ' + jsonKey + ';\n'
            out +=  genGetFunc(getFirstCapital(jsonKey) , jsonKey)
            classDef = getGsonString(jsonDict[jsonKey], getFirstCapital(jsonKey))
            out += classDef
        elif jsonDict[jsonKey] is None:
            print('type is null')
            pass
        else:
            raise ValueError()

    if className != None:
        out += "}\n"
    return out

def mytype(o) :
    if type(o) == type(None):
        print (' type is null %s' % o )
        return type('')
    if type(o) == type(True):
        return type(o)
    try:
        i = int(o)
        return type(1)
    except (ValueError, TypeError):
        try :
            d = float(o)
            return type(0.1)
        except (ValueError,TypeError):
            return type(o)

def genGetFunc(type='', jsonKey=''):
    return 'public '+type+' get' + getFirstCapital(jsonKey) +'(){\nreturn ' + jsonKey + ';\n}\n'          
    
def getFirstCapital(s=''):
    if len(s) >0:
        return s[0].upper() + s[1:]
    else:
        return ''

if __name__ == '__main__':
    main()
