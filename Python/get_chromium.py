"""
    Get Chromium
"""

import sys
import os

import chromium
import dev_sources
import helpers

# Parameters
tag_name = '50.0.2661.102'
working_directory = r'F:\Projects\Amigo\Chromium'
dev_sources_directory_name = 'dev_sources'
dev_branch_name = 'chromium_beta'
dev_sources_name = 'amigo_browser_38'

def MergeChromiumTagAndDevelopmentSources() :
    os.chdir(working_directory)

    base_dir = os.getcwd()

    # Get Chromium tag
    chromium.GetChromium(tag_name)

    exit()

    # Clean Chromium sources
    os.chdir(chromium.chromium_sources)
    dev_sources.CleanChromiumSources()
    os.chdir(base_dir)
    
    # Get Dev sources
    helpers.CheckNotExistDir(dev_sources_name, 'Exsist development sources directory!')
    dev_sources.CloneDevSources(dev_branch_name)
    
    # Old Size 
    was_dev_size = helpers.GetSizeFolder(dev_sources_name)

    # Prepare for merge (Remove all except .git) 
    helpers.CheckExistDir(dev_sources_name, 'Development sources directory NOT exists!')
    helpers.RemoveAllExcept(dev_sources_name, ['.git'])
    
    # Copy chromium sources
    helpers.BatchCommand(r'xcopy {}\* {} /E /Q /Y /H'.
        format(os.path.join(base_dir, chromium.chromium_sources), dev_sources_name))

    # New Size 
    new_dev_size = helpers.GetSizeFolder(dev_sources_name)

    # Print diff size of sources
    if was_dev_size != new_dev_size :
        print('*'*30)
        print('!!! Warning !!! was {} MB new {} MB'.format(was_dev_size, new_dev_size))
        print('*'*30)

    # Prepare and commit
    os.chdir(dev_sources_name)
    os.rename(r'.\src\.gitignore', r'.\src\.gitignore_new')
    helpers.BatchCommand(r'git add --all')
    helpers.BatchCommand(r'git add -u')
    helpers.BatchCommand(r'git commit -m "Chromium beta {} all commit"'.format(tag_name))
    os.rename(r'.\src\.gitignore_new', r'.\src\.gitignore')
    helpers.BatchCommand(r'git add .\src\.gitignore')
    helpers.BatchCommand(r'git commit -m "Chromium beta {}"'.format(tag_name))
    os.chdir(base_dir)

if __name__ == '__main__' :
    MergeChromiumTagAndDevelopmentSources()
    input("Press enter to exit ;)")
                            
              
