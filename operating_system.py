#new file is here
#this is the develop branch
from __future__ import annotations
python_list = []


class Folder:
    def __init__(self, folder : Folder = ""):
        self._folder = folder
    
    def set_contents(self, folder: Folder = "", file: File = ""):
        self._list = []
        self._list.append(file)
        self._list.append(folder)
    
    def current_directory(self):
        self._current_directory = current_directory
    
    def mkdir(self, folder_name: Folder):
        self._new_folder = folder_name
        self._folder.set_contents(self._new_folder)

    def cd(self, destination):
        self._destination = destination
        if self._destination in self._list:
            self._folder.current_directory()
        else:
            raise FileNotFoundError()
    
    def rm(self, folder):
        self._folder.set_contents.remove(folder)
    
    def get_contents(self):
        return self._folder.current_directory()

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






