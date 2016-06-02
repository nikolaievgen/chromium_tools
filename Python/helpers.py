"""
    Common routines   
"""

import sys
import os
import subprocess

class AppError(Exception):
    def __init__(self, err):
        self.err_ = err
    def __str__(self):
        return repr(self.err_)

def CheckNotExistDir(name, err_descr) :
    if os.path.isdir(name) :
        raise AppError(err_descr)

def CheckNotExistDir(name, err_descr) :
    if os.path.isdir(name) :
        raise AppError(err_descr)

def CheckIsEmptyDir(name, err_descr) :
    if os.listdir(name) != [] :
        raise AppError(err_descr)

def CheckIsNotEmptyDir(name, err_descr) :
    if os.listdir(name) == [] :
        raise AppError(err_descr)
    
def CheckAndCreateDir(name, err_descr) :
    CheckNotExistDir(name, err_descr)
    os.mkdir(name)
    os.chdir(name)   

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

def SystemOutput(command) :
    bin_out = subprocess.check_output(command, shell=True)
    out = bin_out.decode('cp866')
    return out

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
    
    if os.path.isdir(one) :
        shutil.rmtree(one, onerror=onerror)
        print('    Remove done!')
    else :
        print('    No directory!')

def RemoveAllExcept(where, except_list) :
    dir_list = os.listdir(where)
    for item in dir_list :
        if item not in except_list :
            item = os.path.join(where, item)
            RemoveDirectory(item)
