import os
from posixpath import dirname
path="D:\My Photos\old photos"
for dirpath , dirname,filename, in os.walk(path):
    print(f'Path :{dirpath}')
    print(f'Dir: {dirname}')
    print(f'File: {filename}')
    print('-------------------'
