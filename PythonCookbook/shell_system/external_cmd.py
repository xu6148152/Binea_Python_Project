#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import subprocess

# try:
#     out_bytes = subprocess.check_output(['netstat', '-a'], timeout=5)
#     out_text = out_bytes.decode('utf-8')
#     print(out_bytes)
# except subprocess.CalledProcessError as e:
#     out_bytes = e.output
#     code = e.returncode
#
# except subprocess.TimeoutExpired as e:
#     out_bytes = e.output

# Some text to send
text = b'''
hello world
this is a test
goodbye
'''

# Launch a command with pipes
p = subprocess.Popen(['wc'],
          stdout = subprocess.PIPE,
          stdin = subprocess.PIPE)

# Send the data and get the output
stdout, stderr = p.communicate(text)

# To interpret as text, decode
out = stdout.decode('utf-8')
# err = stderr.decode('utf-8')
