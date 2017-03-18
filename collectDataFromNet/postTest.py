#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import requests


def simple_post_test():
    params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
    r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
    print(r.text)


def cookie_test():
    params = {'username': 'Ryan', 'password': 'password'}
    r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
    print("Cookie is set to:")
    print(r.cookies.get_dict())
    print("------------------")
    print("Going to profile page...")
    r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
    print(r.text)


def session_test():
    session = requests.Session()

    params = {'username': 'username', 'password': 'password'}
    s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
    print("Cookie is set to:")
    print(s.cookies.get_dict())
    print("-----------------")
    print("Going to profile page...")
    s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
    print(s.text)

def auth_test():
    from requests.auth import AuthBase
    from requests.auth import HTTPBasicAuth

    auth = HTTPBasicAuth('ryan', 'password')
    r = requests.post(url="http://pythonscraping.com/pages/auth/login.php",auth=auth)
    print(r.text)


if __name__ == '__main__':
    auth_test()