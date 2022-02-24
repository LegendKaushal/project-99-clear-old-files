import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token



    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from):
            for name in files:
                local_path = os.path.join(root, name)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)

                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode = WriteMode('overwrite')) 
        

def main():
    access_token = "LDTgpoKda3MAAAAAAAAAAWPaQbkiEHCkVbFjHLAyoB91C5uSr685tqcz-PnShJ2n"
    transferData = TransferData(access_token)
    file_from = str(input("enter the folder path: "))
    file_to = input("enter the folder path: ")
    transferData.upload_file(file_from,file_to)
    print("file has been moved")
main()