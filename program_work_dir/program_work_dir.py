import os
import sys
import configparser


def verify_client_folder():
    """Check for the working directory. If does not exist, then call the class ClientFolder() that creates it."""

    

    # get name of the client program
    client=os.path.basename(__file__)
    client_folder_name=client.split('.')[0]
    print(client_folder_name)

    # search for the C:\\parent_folder\
    verify=os.path.exists(f'C:\\{client_folder_name}')

    print(verify)

    # if found then return. if not found then call ClientFolder

    if verify==False:
        client_folder=os.makedirs(f'C:\\{client_folder_name}')
        return client_folder
    else:
        return f'C:\\{client_folder_name}'



    

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
            return self.client_folder
        else:
            return f'C:\\{self.client_folder_name}'




class WorkDirectory():
    """ This is the directory for configuartion files, data storage, temporary folders, etc. """
    def __init__(self,client_folder):
        self.client_folder=client_folder
        print(self.client_folder)

    def make(self,project):
        os.makedirs(f'C:\\{client_folder_name}\\{project}')



class ConfigFile():
    """Creates client configuration (.ini) files as needed by the client software"""
    pass


# a=ClientFolder()