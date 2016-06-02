"""
    Get Chromium
"""

import sys
import os

import chromium
import dev_sources
import helpers

# Parameters
tag_name = '47.0.2526.111'
new_directory_dev_sources_name = 'dev_sources'

def MergeChromiumTagAndDevelopmentSources() :
    base_dir = os.getcwd()

    chromium.GetChromium(tag_name)

    os.chdir(chromium.chromium_sources)
    dev_sources.CleanChromiumSources()
    os.chdir(base_dir)
    
    helpers.CheckNotExistDir(new_directory_dev_sources_name, 'Exsist development sources directory!')
    dev_sources.CloneDevSources(branch_name)
    
    helpers.CheckExistDir(new_directory_dev_sources_name, 'Development sources directory NOT exists!')
    helpers.RemoveAllExcept(new_directory_dev_sources_name, ['.git'])
    
    pass

'''
0. get chromium
0. create chromium clean
1. git clone -b my-branch git@github.com:user/myproject.git
2. calculate all size1
2. remove in dir all except .git
3. copy all from chromium clean
xcopy .\* f:\Projects\Amigo\Chromium1\Amigo\amigo_browser_38 /S /Q

4. rename .git ignore as git ignore new
5. git add --all 
6. git add -u
6. calculate all size2
7. compare size1 and size2 need commit?
7. parse git diff
7. git commit -m "[major] Chromium beta 38.0.2125.77"
8. rename as .git ignore
9. git commit -m "[major] Chromium beta 38.0.2125.77"

'''  


if __name__ == '__main__' :
    GetChromium()
                            
              
