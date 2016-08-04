"""
    Common routines   
"""

import sys
import os
import subprocess
import shutil

# common exeception type for errors
class AppError(Exception):
  def __init__(self, err):
    self.err_ = err
  def __str__(self):
    return repr(self.err_)

# check directory not exist
# if not throw exception
def CheckNotExistDir(name, err_descr) :
  if os.path.isdir(name) :
    raise AppError(err_descr)

# check directory is exist
# if not throw exception
def CheckExistDir(name, err_descr) :
  if not os.path.isdir(name) :
    raise AppError(err_descr)

# check directory is empty
# if not throw exception
def CheckIsEmptyDir(name, err_descr) :
  if os.listdir(name) != [] :
    raise AppError(err_descr)

# check directory is not empty
# if not throw exception
def CheckIsNotEmptyDir(name, err_descr) :
  if os.listdir(name) == [] :
    raise AppError(err_descr)
    
# check directory is not exist, create and change current directory
def CheckAndCreateDir(name, err_descr) :
  CheckNotExistDir(name, err_descr)
  os.mkdir(name)
  os.chdir(name)   

# run command in cmd
# collect errors, output and input command
# todo 
# locale parameter?
def BatchCommand(command) :
  p = subprocess.run(command,  shell=True,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT)
  delim_str = '-'*(len(command)+ 20)
  print(delim_str)
  print("Command " + str(command) + " OUT >>> ")
  print(delim_str)
  out = p.stdout.decode('cp866')
  print(out)
  return out

# remove directory recursively
# 1. shutil.rmtree()
# 2. when error, attempt set access write
# 3. if error, attempt remove as batch command
def RemoveDirectory(one) :
  one = os.path.abspath(one)
  print('    Attempt to remove directory: ', one)
  def onerror(func, path, exc_info):
    """
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.

    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """
    import stat
    if not os.access(path, os.W_OK):
      # Is the error an access error ?
      os.chmod(path, stat.S_IWUSR)
      func(path)
    else:
      raise
    
  try :
    if os.path.isdir(one) :
      shutil.rmtree(one, onerror=onerror)
      print('    Remove done!')
    else :
      print('    No directory!')
  except Exception as inst :
    print('Remove directory exception!')
    print(inst)
    print('Force deleting!')
    # force deleting
    BatchCommand(r'rmdir /S /Q {}'.format(one))
    CheckNotExistDir(one, 'Error directory removing!')

# copy one file, log error operation in output
def CopyFile(src, dst) :
  try :
    shutil.copy2(src, dst)
  except OSError as why :
    print("Error copy file : {}, cause : !".format(src, why.strerror))

# copy and create dir, log operation in output
def CopyCreateDirectory(src, dst) :
  shutil.copytree(src, dst, False, None, CopyFile);

# copy dir contents from src to dst
def CopyDirectory(src, dst) :
  names = os.listdir(src)
  for name in names:
    srcname = os.path.join(src, name)
    dstname = os.path.join(dst, name)
    if os.path.isdir(srcname):
      CopyCreateDirectory(srcname, dstname)
    else:
      CopyFile(srcname, dstname)

# remove dir contents except files in except_list
def RemoveAllExcept(where, except_list) :
  print("Remove dir contents from {}".format(where))
  dir_list = os.listdir(where)
  for item in dir_list :
    if item not in except_list :
      item = os.path.join(where, item)
      if os.path.isfile(item) :
        os.remove(item)
      else :
        RemoveDirectory(item)
    else:
      print("except list item : {}".format(item))
        
# calculate directory contents size
def GetSizeFolder(start_path):
  total_size = 0
  for dirpath, dirnames, filenames in os.walk(start_path):
    for f in filenames:
      fp = os.path.join(dirpath, f)
      total_size += os.path.getsize(fp)
  return total_size

# logging helper
# todo - set filename as option param
class PrintLogger:
  def __init__(self, filename):
    self.terminal = sys.stdout
    self.log = open(filename, "w")

  def write(self, message):
    self.terminal.write(message)
    self.log.write(message)