"""
    Check and start merge chromium procedure
"""

import sys
import os
import datetime

import merge_chromium
import config_params    
import helpers

"""
  Make merge chromium
"""
def RunMergeChromium(tag) :
  # parameters
  config_params.tag_name = tag
  config_params.working_directory = GetWorkingDirectory()
        
  if config_params.tag_name and os.path.isdir(config_params.working_directory) :
    # enable logging
    log_file = os.path.join(config_params.working_directory, config_params.log_file_name)
    sys.stdout = helpers.PrintLogger(log_file)

    merge_chromium.MergeChromium()

"""
  Determine directory where to make merge
"""
def GetWorkingDirectory() :
  # root directory is parent dir
  names = os.listdir(config_params.root_working_directory)
  count_working_items = len(names)
        
  print('Root directory has {} items'.format(count_working_items))

  # check max count work dir's in root
  # when exceeds max, remove oldest
  if(count_working_items > config_params.max_count_working_items - 1) :
    path_names = {}
    creations = []
    # sort working items by creation times
    for name in names :
      path_name =  os.path.join(config_params.root_working_directory, name)
      stat = os.stat(path_name)
      creations.append(stat.st_ctime)
      path_names[stat.st_ctime] = path_name

    # remove oldest
    if(len(creations) > 0 and len(path_names) > 0 ) :
      print('Need to remove the oldest working dir!')
      creations.sort()
      to_remove = path_names[creations[0]]
      print('Remove {} directory'.format(to_remove))
      helpers.RemoveDirectory(to_remove)

  # create new working dir
  new_working_dir = os.path.join(config_params.root_working_directory, datetime.datetime.now().strftime('%m_%d_%H_%M'))
  os.makedirs(new_working_dir)

  return new_working_dir

"""
  Check need run merge chromium src in development sources
"""
def CheckNeedMerge() :
  # check exist beta file
  if os.path.isfile(config_params.new_beta_file) :
    # read tag from beta file file
    tag = ''
    with open(config_params.new_beta_file) as f :
      tag = f.readline().strip()
    os.remove(config_params.new_beta_file)

    if tag :
      # run merge
      RunMergeChromium(tag)

if __name__ == '__main__' :
  print('Merge starter is run!')
  CheckNeedMerge()