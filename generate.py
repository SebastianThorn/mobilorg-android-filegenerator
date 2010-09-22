#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys,  os, hashlib
files =  os.listdir('.')
files.remove('generate.py')
files.remove('checksums.dat')
files.remove('index.org')

## Creating index.org

header = "#+READONLY\n#+TODO: TODO DONE\n#+TAGS:\n#+DRAWERS:\n#+ALLPRIORITIES: A B C\n"
f = open('index.org', 'w')
f.write(header)
for file in files:
    f.write('* [[file:' + file + '][' + file[:-4] + ']]\n')
files.append('index.org')
f.close()


## Creating the checksums.dat

checksums = ""
for file in files:
    f = open(file,'rb')
    m = hashlib.md5()
    while True:
        ## Don't read the entire file at once...
        data = f.read(10240)
        if len(data) == 0:
            break
        m.update(data)
    checksums += (m.hexdigest() + ' ' + file + '\n')
checksums = checksums[:-1]
f.close()
f = open('checksums.dat','w')
f.write(checksums)
f.close()
