# -*- coding: utf-8 -*- 
# Functions to talk with FileSystem
import zipfile
import os
import sys
from filehash import FileHash
import subprocess
import threading
import shutil
import time

#Addr to put program in background, using Popen()
DETACHED_PROCESS = 0x00000008

def Decompress_thezip(path,output):
 fz = zipfile.ZipFile(path, 'r')
 ret = fz.testzip()
 if ret is not None:
  print ("First bad file in zip: "+ ret)
  return False
 for file in fz.namelist():
  fz.extract(file, output)
 fz.close()
 return True

# recursive func get files and return array of strings with file names
def GetFilesByDir(d):
 fileslist = []
 if not os.path.isdir(d):
  fileslist.append(d)
 else:
  for item in os.listdir(d):
   fileslist.extend(GetFilesByDir((d + '/' + item) if d != '/' else '/' + item))
 return fileslist

# get full path of file, open the file and return HASH sha256
def GetHash(input):
 hash = FileHash('sha256')
 return hash.hash_file(input)

# Rename all long filenames to short filenames
def ChangeNamesFiles(path_out): 
 i=0
 for filename in os.listdir(path_out):
  name, file_extension = os.path.splitext(filename)
  dst = str(i) + file_extension
  src = path_out +"/"+ filename 
  dst = path_out +"/"+ dst 
  os.rename(src, dst) 
  i += 1

# find string on file, if ok return True
def GrepFile(fname, txt):
 with open(fname) as content:
  return any(txt in line for line in content)

# Execute all program list
def ExecuteAllPrograms(ExecutablesFiles):
 for program in ExecutablesFiles:
  subprocess.Popen(program,creationflags=DETACHED_PROCESS)

# Remove all dir contents
def ClearDir(path):
 for c in os.listdir(path):
  full_path = os.path.join(path, c)
  if os.path.isfile(full_path):
   os.remove(full_path)
  else:
   shutil.rmtree(full_path)



