
from zipfile import ZipFile

with ZipFile('django_backup.zip', 'r') as zipObj:
    
   zipObj.extractall('django')