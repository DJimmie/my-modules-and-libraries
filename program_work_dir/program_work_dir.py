import os
import sys
import configparser



class ClientFolder():
    """Creates the client software's parent folder as follows 
        -C:\\parent_folder\\working_dir\\
        -When possible the parent folder will take the name of the program (client) that is using program_work_dir.py.
        -The working directories are created in the WorkDirectory class"""
    
    client_folder=None
    def __init__(self,client):
        # get name of the client program
        self.client=client #os.path.basename(__file__)
        self.client_folder_name=self.client.split('.')[0]
        
        ClientFolder.client_folder=self.verify_client_folder()
    
    def __str__(self):
        return str(self.client_folder_name)
    
    def verify_client_folder(self):
        """Check for the working directory. If does not exist, then call the class ClientFolder() that creates it."""

        # search for the C:\\parent_folder\
        verify=os.path.exists(f'C:\\{self.client_folder_name}')

        print(verify)

        # if found then return. if not found then call ClientFolder

        if verify==False:
            self.client_folder=os.makedirs(f'C:\\{self.client_folder_name}')
            ConfigFile(self.client_folder_name)
            return self.client_folder
        else:
            return f'C:\\{self.client_folder_name}'




class WorkDirectory():
    """ This is the directory for configuartion files, data storage, temporary folders, etc. """
    def __init__(self,client_sub_folder,client_folder):
        self.client_folder=client_folder
        self.client_sub_folder=client_sub_folder
        print(self.client_sub_folder)
        self.make()

    def make(self):
        try:
            os.makedirs(f'C:\\{self.client_folder}\\{self.client_sub_folder}')
        except FileExistsError:
            return

        

class ConfigFile():
    """Creates client configuration (.ini) files as needed by the client software"""


    def __init__(self,client_folder):

        self.client_folder=client_folder
        self.config=configparser.ConfigParser()
        self.config_defaults()

    def config_defaults(self):

        self.config['DATABASE SERVER']= {'ServerLocation':'path'}

        config_file=f'C:\\{self.client_folder}\\{self.client_folder}.ini'
        with open(config_file, 'w') as configfile:
            self.config.write(configfile)

    


# a=ClientFolder()