import os
import shutil
import time

deleted_folders_count = 0
deleted_files_count = 0
path = "D:\\Whitehat Jr\\trash"
days = 1
seconds = time.time(-days)

if os.path.exists(path):

    for root_folder, folders, files in os.walk(path):
        c_time = os.stat(path).st_ctime

        if seconds>=c_time:

            if not shutil.rmtree(path):
                print("Folder is removed succesfully")
            else:
                print("Unable to delete the "+path)