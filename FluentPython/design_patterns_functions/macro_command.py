#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class MacroCommand:
    def __init__(self, commands):
        self.commands = list(commands)

    def __call__(self):
        for command in self.commands:
            command()
