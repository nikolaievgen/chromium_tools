"""
    Check and start merge chromium procedure
"""

import sys
import os
import datetime

import get_chromium
import config_params    
import helpers

def RunMergeChromium(tag) :
    config_params.tag_name = tag
    config_params.working_directory = GetWorkingDirectory()
        
    if config_params.tag_name and os.path.isdir(config_params.working_directory) :
        log_file = os.path.join(config_params.working_directory, config_params.log_file_name)
        sys.stdout = helpers.PrintLogger(log_file)

        get_chromium.MergeChromium()

def GetWorkingDirectory() :
    names = os.listdir(config_params.root_working_directory)
    count_working_items = len(names)
        
    print('Root directory has {} items'.format(count_working_items))

    if(count_working_items > config_params.max_count_working_items - 1) :
        path_names = {}
        creations = []
        # sort working items by creation times
        for name in names :
            path_name =  os.path.join(config_params.root_working_directory, name)
            stat = os.stat(path_name)
            creations.append(stat.ctime)
            path_names[stat.ctime] = path_name

        # remove oldest
        if(len(creations) > 0 and len(path_names) > 0 ) :
            print('Need to remove the oldest working dir!')
            creations.sort()
            to_remove = path_names[creations[0]]
            print('Remove {} directory'.format(to_remove))
            helpers.RemoveDirectory(to_remove)

    new_working_dir = os.path.join(config_params.root_working_directory, datetime.datetime.now().strftime('%m_%d_%H_%M'))
    os.makedirs(new_working_dir)

    return new_working_dir

def CheckNeedMerge() :
    if os.path.isfile(config_params.new_beta_file) :
        tag = ''
        with open(config_params.new_beta_file) as f :
            tag = f.readline().strip()
        #os.remove(config_params.new_beta_file)

        if tag :
            RunMergeChromium(tag)

if __name__ == '__main__' :
    print('Chromium starter is run!')
    CheckNeedMerge()