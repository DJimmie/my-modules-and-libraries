import program_work_dir as pwd
import os

## Creating client folder

x={'database server':{'jim':1,'dog':'Cat'}}

client=pwd.ClientFolder(os.path.basename(__file__),x)

# config_file=f'C:\\{client}\\{client}.ini'

print(config_file)

print(pwd.ClientFolder.client_folder)



## Cretating subfolders of the client folder

# pwd.WorkDirectory('DD',client_folder=client,)


## create config file

# pwd.ConfigFile(client)