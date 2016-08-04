"""
    Dev sources utilities
"""
import sys
import os
import subprocess
import shutil
import time

from helpers import (AppError, BatchCommand, CheckAndCreateDir, RemoveDirectory)

# clone development sources
def CloneDevSources(branch_name, repository_url) :
  print("Clone development sources")

  BatchCommand("git clone -b {} {}".format(branch_name, repository_url))
    
  print("Clone development sources done!")
                   
# clean chromium sources, delete unused massive tests, etc 
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
