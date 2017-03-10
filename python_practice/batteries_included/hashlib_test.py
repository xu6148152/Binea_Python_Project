# coding=utf-8
import hashlib
import re

__author__ = 'xubinggui'

#摘要算法

#MD5
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()

#sha-1
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

salt = 'abc'

def login(username,password):

    if db.has_key(username):

        md5_test=hashlib.md5()

        md5_test.update(password+username+salt)

        md5_1=md5_test.hexdigest()

        if md5_1==db.get(username, 0):

            print 'Congratulations! Authentication Passed!'

        else:

            print 'Password Error!Please try again.'

    else:

        print 'Username was not exist!'


salt='5580c38c87f0410ad153'

def register(username, password):

    m1=re.match('^[a-zA-z\_][a-zA-Z0-9\_]{3,19}',username)

    if m1:

        m2=re.match('[0-9a-zA-Z]{6,20}',password)

        if m2:

            md5_test=hashlib.md5()

            md5_test.update(password+username+salt)

            md5=md5_test.hexdigest()

            db[username]=md5

        else:

            print '密码为字母和数字的组合，长度介于6-20位之间！'

    else:

        print '用户名必须以字母或者下划线开头'