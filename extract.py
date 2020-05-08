from zipfile import ZipFile
with ZipFile(input() + '.zip', 'r') as zipObj:
    zipObj.extractall()
    '''
     It will by default extract all the files in the same directory
    If you want a specific directory enter the full path like:  D:\Projects
    '''
