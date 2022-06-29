#!/usr/bin/env python3
"""
File Operations
"""

class FileOperation():
    
    # private function
    def __readAllLines(self):
        # different modes for file operation (r,w,a,+), defualt is read
        file = open('sample.txt', 'r')
        for line in file:
            print(line.rstrip())
            
    # single underscore is not restriction
    def _cloneFile(self):       
        # write a copy of file
        fileopen = open('sample.txt', 'rt')
        #if no such file exist py will create one
        filewrite = open('sample-copy.txt', 'wt')
        for line in fileopen:
            # write file, rstrips strips end of file
            print(line.rstrip(), file = filewrite, end='\n')
            # we can write files like this but not preffered since print can strip line ending regardless of OS
            # filewrite.writelines(line)
            print('.', end='', flush=True)
        # close the write file important since the buffering data loss prevent
        filewrite.close();
            
file = FileOperation()
# name mangling a magic wand of python allows access private variable
file._FileOperation__readAllLines()
file._cloneFile()