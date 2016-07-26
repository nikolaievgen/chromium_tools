"""
    Get Chromium
"""

import sys
import os
import argparse

import chromium
import dev_sources
import helpers
import config_params    

def MergeChromium() :
    # set working directory
    os.chdir(config_params.working_directory)

    base_dir = os.getcwd()

    # Get Chromium tag
    chromium.GetChromium(config_params.tag_name)

    # first stage
    #exit()

    # Clean Chromium sources
    os.chdir(chromium.chromium_sources)
    dev_sources.CleanChromiumSources()
    os.chdir(base_dir)
    
    # Get Dev sources
    helpers.CheckNotExistDir(config_params.dev_sources_name, 'Exsist development sources directory!')
    dev_sources.CloneDevSources(config_params.dev_branch_name, config_params.dev_repository_url)
    
    one_mb = (1024 * 1024)
    # Old Size 
    was_dev_size = helpers.GetSizeFolder(config_params.dev_sources_name) / one_mb

    # Prepare for merge (Remove all except .git) 
    helpers.CheckExistDir(config_params.dev_sources_name, 'Development sources directory NOT exists!')
    helpers.RemoveAllExcept(config_params.dev_sources_name, ['.git'])
    
    # Copy chromium sources
    # helpers.BatchCommand(r'xcopy {}\* {} /E /Q /Y /H'.
    #    format(os.path.join(base_dir, chromium.chromium_sources), config_params.dev_sources_name))
    helpers.CopyDirectory(os.path.join(base_dir, chromium.chromium_sources), config_params.dev_sources_name)

    # New Size 
    new_dev_size = helpers.GetSizeFolder(config_params.dev_sources_name) / one_mb

    # Print diff size of sources
    if was_dev_size != new_dev_size :
        print('*'*30)
        print('!!! Warning !!! was {} MB new {} MB'.format(was_dev_size, new_dev_size))
        print('*'*30)

    # Prepare and commit
    os.chdir(config_params.dev_sources_name)
    os.rename(r'.\src\.gitignore', r'.\src\.gitignore_new')
    helpers.BatchCommand(r'git add --all')
    helpers.BatchCommand(r'git add -u')
    helpers.BatchCommand(r'git commit -m "Chromium beta {} all commit"'.format(config_params.tag_name))
    os.rename(r'.\src\.gitignore_new', r'.\src\.gitignore')
    helpers.BatchCommand(r'git add .\src\.gitignore')
    helpers.BatchCommand(r'git commit -m "Chromium beta {}"'.format(config_params.tag_name))
    #helpers.BatchCommand(r'git push origin')

    os.chdir(base_dir)

if __name__ == '__main__' :
    # process arguments
    parser = argparse.ArgumentParser("Merging chromium tag")
    parser.add_argument('--tag')
    parser.add_argument('--dir')
    args = vars(parser.parse_args(sys.argv[1:]))

    if 'tag' in args :
        config_params.tag_name = args['tag']

    if 'dir' in args:
        config_params.working_directory = args['dir']

    MergeChromium()

    input("Press enter to exit ;)")
