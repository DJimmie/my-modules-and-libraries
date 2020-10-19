import program_work_dir as pwd
import os

## Creating client folder
client=pwd.ClientFolder(os.path.basename(__file__))

print(pwd.ClientFolder.client_folder)


## Cretating subfolders of the client folder

# pwd.WorkDirectory('DD',client_folder=client,)


## create config file

# pwd.ConfigFile(client)