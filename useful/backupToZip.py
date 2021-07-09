#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
    #Back up the entire contents of 'folder' into a ZIP file
    
    folder = os.path.abspath(folder) #make sure folder path is absolute, not rel
    
    #Figure out the filename this code should use based on 
    #what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder)+ '_' +str(number) + '.zip'
        if not os.path.exists(zipFilename): #iterate through possible versions
            break
        number += 1 #if it already exists keep going, otherwise break
    
    #Create the ZIP file
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    
    #Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding the files from {foldername}...')
        #Add the current folder to the ZIP file.
        backupZip.write(foldername)
        
        #Add all the files in this folder to the ZIP
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue #don't back up the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done')

