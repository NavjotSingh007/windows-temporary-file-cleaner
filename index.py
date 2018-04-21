import os
import shutil
    
folder = 'C:/Users/'+os.getlogin()+'/AppData/Local/Temp'

deleteFileCount = 0
deleteFolderCount = 0

for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
            deleteFileCount = deleteFileCount + 1

        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
            deleteFolderCount = deleteFolderCount + 1

    except Exception as e:
        print(e)

print(str(deleteFileCount)+' files and '+ str(deleteFolderCount)+' folders deleted.')