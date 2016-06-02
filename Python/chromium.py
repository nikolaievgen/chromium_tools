"""
    Chromium utilities
"""

import sys
import os

from helpers import (AppError, BatchCommand, CheckAndCreateDir)

# Main parameters
chromium_root_name = 'chromium'
chromium_sources_name = 'chromium_src'
chromium_sources = os.path.join(chromium_root_name, chromium_sources_name)

# Get depot tools
def GetDepotTools(depot_name = 'depot_tools') :
    print('  Get Depot tools')
    url_depot = 'https://storage.googleapis.com/chrome-infra/depot_tools.zip'
    depot_zip_name = 'depot_tools.zip'

    CheckAndCreateDir(depot_name, 'Exsist depot directory!')

    depot_archive = os.path.join(os.getcwd(), depot_zip_name)

    print('  Url query depot tools')
    import urllib.request
    url_opener = urllib.request.URLopener()
    url_opener.retrieve(url_depot, depot_archive)

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
def GetChromiumSources(chromium_sources_name = 'chromium_browser') :
    print('  Get chromium sources')
    CheckAndCreateDir(chromium_sources_name, 'Exsist chromium sources directory!')
    BatchCommand('fetch --nohooks chromium')
    
    # return to original
    os.chdir('..')
    
# Get needed tag
def GetChromiumTag(tag) :
    print('  Get needed tag')

    # we must be in chromium sources directory
    if not os.path.isdir('./src') :
        raise AppError('No src directory!')
    
    os.chdir('./src')
    comnds = '''git fetch origin
    git stash
    git checkout tags/{}
    gclient sync --with_branch_heads --nohooks'''.format(tag)
    list(map(BatchCommand, comnds.splitlines(True)))
    # return to original
    os.chdir('..')
    
def GetChromium(tag) :      
    print('GetChromium Started')
    
    # Root directory
    CheckAndCreateDir(chromium_root_name, 'Exsist root directory!')

    GetDepotTools()
    GetChromiumSources(chromium_sources_name)
    os.chdir(chromium_sources_name)
    GetChromiumTag(tag)

    # return to original
    os.chdir('../..')
        
    print('GetChromium Finished success')

if __name__ == '__main__' :
    GetChromium()
                            
              
