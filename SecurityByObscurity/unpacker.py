import zipfile
import os
import lzma
import bz2
import gzip

count = 0

## Standard Zip ##
workingfile = '2cdc6654fb2f8158cd976d8ffac28218b15d052b5c2853232e4c1bafcb632383.zip'
zip_ref = zipfile.ZipFile(workingfile, 'r')
oldfile = workingfile
workingfile = zip_ref.infolist()[0].filename
zip_ref.extract(workingfile)
zip_ref.close()

while zipfile.is_zipfile(workingfile):
    zip_ref = zipfile.ZipFile(workingfile, 'r')
    oldfile = workingfile
    workingfile = zip_ref.infolist()[0].filename
    zip_ref.extract(workingfile)
    zip_ref.close()
    os.remove(oldfile)
    count += 1

os.rename(workingfile, 'test')
workingfile = 'test'

## LZMA ##
while True:
    try:
        f = lzma.open(workingfile)
        f_content = lzma.decompress(f.read())
        thing = open('test', 'wb')
        thing.write(f_content)
        thing.close()
        workingfile = thing.name
        count += 1
    except:
        break


## BZ2 ##
while True:
    try:
        f = bz2.open(workingfile)
        f_content = bz2.decompress(f.read())
        thing = open('test', 'wb')
        thing.write(f_content)
        thing.close()
        workingfile = thing.name
        count += 1
    except:
        break

## GZIP ##
while True:
    try:
        f = gzip.open(workingfile)
        f_content = gzip.decompress(f.read())
        thing = open('test', 'wb')
        thing.write(f_content)
        thing.close()
        workingfile = thing.name
        count += 1
    except:
        break


## Decrypt ##

zip_ref = zipfile.ZipFile(workingfile, 'r')
oldfile = workingfile
workingfile = zip_ref.infolist()[0].filename

f = open('10-million-password-list-top-1000000.txt')

while True:
    try:
        line = f.readline().strip('\n')
        zip_ref.setpassword(str.encode(line))
        zip_ref.extract(workingfile)
        print(line)
        print(open(workingfile).read())
        break
    except:
        pass

zip_ref.close()



