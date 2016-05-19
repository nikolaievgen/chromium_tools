"""
Get Chromium
"""

import sys
import os

class AppError(Exception):
    def __init__(self, err):
        self.err_ = err
    def __str__(self):
        return repr(self.err_)
    
def CheckAndCreateWorkDir(name, err_descr) :
    if os.path.isdir(name) :
        raise AppError('Exsist root directory!')
    os.mkdir(name)
    os.chdir(name)   

print('GetChromium Started')

# Main parameters
root_name = 'chrome'
tag = '47.0.2526.111'
depot_name = 'depot_tools'
browser= 'chromium_browser'

# Root directory
CheckAndCreateWorkDir(root_name, 'Exsist root directory!')

# Get depot tools
print('  Get Depot tools')
url_depot = 'https://storage.googleapis.com/chrome-infra/depot_tools.zip'
depot_zip_name = 'depot_tools.zip'

CheckAndCreateWorkDir(depot_name, 'Exsist depot directory!')

depot_archive = os.path.join(os.getcwd(), depot_zip_name)

import urllib.request
url_opener = urllib.request.URLopener()
url_opener.retrieve(url_depot, depot_archive)

print('  Extracting Depot tools')
import zipfile
with zipfile.ZipFile(depot_archive) as zip_archive:
    zip_archive.extractall()
os.remove(depot_archive)

# Clean
if true :
    import shutil
    os.chdir('../..')
    shutil.rmtree(os.path.abspath(os.path.join(os.getcwd(), root_name)))
                              
              
