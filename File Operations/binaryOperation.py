#!/usr/bin/env python3
"""
Binary File Operations
"""

class BinaryFileOperation():
    
    def binaryWrite(self):
        fileopen = open('robotech.jpeg', 'rb')
        filewrite = open('robotech-copy.jpeg', 'wb')
        while True:
            # read file partially with some buffer size for better memory management, here 10kb
            buffer = fileopen.read(10240)
            if buffer:
                filewrite.write(buffer)
                print('.', end='', flush=True)
            else: break
        filewrite.close()
        print('\nfinished....')

binary = BinaryFileOperation()
binary.binaryWrite()