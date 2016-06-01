import sys
import os
import subprocess
import shutil

class AppError(Exception):
    def __init__(self, err):
        self.err_ = err
    def __str__(self):
        return repr(self.err_)

def RemoveDirectoryTree(one) :
    one = os.path.abspath(one)
    print('    Remove garbage: ', one)
    def onerror(func, path, exc_info):
        """
        Error handler for ``shutil.rmtree``.

        If the error is due to an access error (read only file)
        it attempts to add write permission and then retries.

        If the error is for another reason it re-raises the error.

        Usage : ``shutil.rmtree(path, onerror=onerror)``
        """
        import stat
        if not os.access(path, os.W_OK):
            # Is the error an access error ?
            os.chmod(path, stat.S_IWUSR)
            func(path)
        else:
            raise
    
    if os.path.isdir(one) :
        shutil.rmtree(one, onerror=onerror)
        print('    Remove done!')
    else :
        print('    No directory!')
            
def PrepareSources() :
    print('Prepare sources start')
    
    if not os.path.isdir('src') :
        raise AppError('No src directory!')
    curr_dir = os.getcwd();

    garbages = [
        r'src\chrometools\test\reference_build',
        r'src\third_party\hunspell_dictionaries',
        r'src\third_party\WebKit\LayoutTests',
        r'src\third_party\WebKit\ManualTests',
        r'src\third_party\WebKit\PerformanceTests'
        ]

    for one in garbages :
        one = os.path.abspath(os.path.join(curr_dir, one))
        RemoveDirectoryTree((one)

    print('Remove git garbages')

    bin_out = subprocess.check_output("dir /b/s/A .git", shell=True)
    out = bin_out.decode('cp866')
    garbages_git = out.splitlines()

    for one in garbages_git :
        RemoveDirectoryTree((one)
        
    print('Remove git garbages done!')
    
    print('Prepare sources Finished success')
'''
0. get chromium
0. create chromium clean
1. git clone -b my-branch git@github.com:user/myproject.git
2. calculate all size1
2. remove in dir all except .git
3. copy all from chromium clean
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
    os.chdir(r'f:\Projects\Amigo')
    os.chdir('Chromium1')
    PrepareSources()
