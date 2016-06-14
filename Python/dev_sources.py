"""
    Dev sources utilities
"""
import sys
import os
import subprocess
import shutil
import time

from helpers import (AppError, BatchCommand, CheckAndCreateDir, RemoveDirectory, SystemOutput)

def CreateDevSources(new_directory_dev_sources_name, branch_name) :
    print("Create development sources")

    CheckAndCreateDir(new_directory_dev_sources_name, 'Exsist development sources directory!')
    
    CloneDevSources(branch_name)

    os.chdir('..')

    print("Create development sources done!")

def CloneDevSources(branch_name) :
    print("Clone development sources")

    BatchCommand(
          "git clone -b {} git@gitlab.corp.mail.ru:amigo/amigo_browser_38.git".format(branch_name)
          )
    
    print("Clone development sources done!")
                   
def CleanChromiumSources() :
    print('CleanChromiumSources sources start')
    
    if not os.path.isdir('src') :
        raise AppError('No src directory!')
    curr_dir = os.getcwd();

    garbages = [
    r'src\chrome\tools\test\reference_build',
    r'src\third_party\hunspell_dictionaries',
    r'src\third_party\WebKit\LayoutTests',
    r'src\third_party\WebKit\ManualTests',
    r'src\third_party\WebKit\PerformanceTests'
    ]

    for one in garbages :
        one = os.path.abspath(os.path.join(curr_dir, one))
        RemoveDirectory(one)

    garbages_git = BatchCommand("dir /b/s/A .git").splitlines()

    for one in garbages_git :
        RemoveDirectory(one)

    print('Remove git garbages done!')
    
    print('CleanChromiumSources sources Finished success')
   
if __name__ == '__main__' :
    os.chdir(r'f:\Projects\Amigo')
    os.chdir('Chromium1')

    '''
    PrepareSources()
    '''

