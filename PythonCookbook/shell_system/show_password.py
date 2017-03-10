#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import getpass

# user = getpass.getuser()
user = input('Enter your username:')
passwd = getpass.getpass()


def svc_login(user, passwd):
    if user == 'binea' and passwd == 'xu743088191':
        return True
    return False


if svc_login(user, passwd):
    print('Yay')
else:
    print('Boo!')
