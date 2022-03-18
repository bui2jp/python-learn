from asyncio import get_child_watcher
import os
import pathlib
import glob
import shutil

print(os.path.isfile('test.txt'))
print(os.path.isdir('test.txt'))

#os.rename('test.txt','text.txt.rename')
#os.symlink

#os.mkdir
#os.rmdir

#pathlib.Path('test.txt').touch()

#shutil.copy()

#print(glob.glob('*'))

#ファイルを含めてフォルダを削除
#shutil.rmtree()

print(os.getcwd())