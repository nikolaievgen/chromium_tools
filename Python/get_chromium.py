"""
Get Chromium
"""

import sys
import os
import subprocess

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

def BatchCommand(command) :
    p = subprocess.run(command,  shell=True,
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE)
    print('-'*(len(command)+ 20))
    print("Command " + str(command) + " OUT >>> ")
    print('-'*(len(command)+ 20))
    p.stdout
        
print('GetChromium Started')

# Main parameters
root_name = 'chrome'
tag = '47.0.2526.111'
depot_name = 'depot_tools'
sources_name= 'chromium_browser'

# Root directory
CheckAndCreateWorkDir(root_name, 'Exsist root directory!')

# Get depot tools
print('  Get Depot tools')
url_depot = 'https://storage.googleapis.com/chrome-infra/depot_tools.zip'
depot_zip_name = 'depot_tools.zip'

CheckAndCreateWorkDir(depot_name, 'Exsist depot directory!')

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
os.environ['Path'] = str(os.getcwd()) + ';' +  os.environ['Path']

os.chdir('..')

# Get chromium sources
print('  Get chromium sources')
CheckAndCreateWorkDir(sources_name, 'Exsist chromium sources directory!')
BatchCommand('fetch --nohooks chromium')

if not os.path.isdir('./src') :
    raise AppError('No src directory!')

# Get needed tag
print('  Get needed tag')
os.chdir('./src')
comnds = '''git stash
git checkout tags/{}
gclient sync --with_branch_heads --nohooks'''.format(tag)
list(map(BatchCommand, comnds.splitlines(True)))

os.chdir('../..')
print('GetChromium Finished success')

# End
os.chdir('..')
sys.exit()

# Clean
if true :
    import shutil
    os.chdir('../..')
    shutil.rmtree(os.path.abspath(os.path.join(os.getcwd(), root_name)))
                              
              
