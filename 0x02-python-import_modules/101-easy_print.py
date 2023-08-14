#!/usr/bin/python3
import os

os.write(1, b'#{} is {}\\n'.format(b'python', b'cool'))
