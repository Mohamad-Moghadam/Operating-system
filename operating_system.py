#new file is here
#this is the develop branch
from __future__ import annotations
python_list = []


class Folder:
    def __init__(self, folder : Folder = ""):
        self._folder = folder
    
    def set_contents(self, file: File = "", folder: Folder = ""):
        self._list = []
        self._list.append(file)
        self._list.append(folder)
    
    def mkdir(self, folder_name: File):
        self._new_folder = folder_name

    def cd():
        pass
    
    def get_contents(self):
        return self._file, self._folder

    def ls(self):
        print(self.get_contents())

    def mv(self, file, destination: Folder):
        if file in self._list:
            self.set_contents(file)
            



class File:
    def __init__(self, file: str = ""):
        self._file = file

    @staticmethod
    def file_det():
        if self._file.endswith(".py"):
            python_list.append(self._file)






