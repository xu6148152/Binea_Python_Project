#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import pyautogui

def test_size():
    print(pyautogui.size())

def test_mouse_move():
    for i in range(10):
        pyautogui.moveTo(100, 100, duration=0.25)
        pyautogui.moveTo(200, 100, duration=0.25)
        pyautogui.moveTo(200, 200, duration=0.25)
        pyautogui.moveTo(100, 200, duration=0.25)

def test_mouse_position():
    print(pyautogui.position())

if __name__ == '__main__':
    test_mouse_position()
