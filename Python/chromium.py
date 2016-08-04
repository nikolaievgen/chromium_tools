"""
    Chromium utilities
    working with chromium repository
"""

import sys
import os

import config_params
from helpers import (AppError, BatchCommand, CheckAndCreateDir)

# chromium sources
chromium_sources = os.path.join(config_params.chromium_root_name, config_params.chromium_sources_name)

# Get depot tools
def GetDepotTools() :
  print('  Get Depot tools')
  CheckAndCreateDir(config_params.depot_name, 'Exsist depot directory!')
  depot_archive = os.path.join(os.getcwd(), config_params.depot_zip_name)

  print('  Url query depot tools')
  import urllib.request
  url_opener = urllib.request.URLopener()
  url_opener.retrieve(config_params.url_depot, depot_archive)

  print('  Extracting Depot tools')
  import zipfile
  with zipfile.ZipFile(depot_archive) as zip_archive:
    zip_archive.extractall()
  os.remove(depot_archive)
  # add dir to PATH
  os.environ['Path'] = str(os.getcwd()) + ';' +  os.environ['Path']
  # return to original
  os.chdir('..')

# Get chromium sources
def GetChromiumSources() :
  print('  Get chromium sources')
  CheckAndCreateDir(config_params.chromium_sources_name, 'Exsist chromium sources directory!')
  BatchCommand('fetch --nohooks chromium')
    
  # return to original
  os.chdir('..')
    
# Get needed tag
def GetChromiumTag() :
  print('  Get needed tag')

  # we must be in chromium sources directory
  if not os.path.isdir('./src') :
      raise AppError('No src directory!')
    
  os.chdir('./src')
  comnds = '''git fetch origin
  git stash
  git checkout tags/{}
  gclient sync --with_branch_heads --nohooks'''.format(config_params.tag_name)
  list(map(BatchCommand, comnds.splitlines(True)))
  # return to original
  os.chdir('..')
    
def GetChromium() :      
  print('GetChromium Started')
    
  # Root directory
  CheckAndCreateDir(config_params.chromium_root_name, 'Exsist root directory!')

  GetDepotTools()
  GetChromiumSources()
  os.chdir(config_params.chromium_sources_name)
  GetChromiumTag()

  # return to original
  os.chdir('../..')
        
  print('GetChromium Finished success')
             
