#new file is here
#this is the develop branch
from __future__ import annotations
python_list = []


class Folder:
    def __init__(self, name: str, folder : Folder = None):
        self.name = name
        self._folder = folder if folder is not None else self
        self._current_directory = ["~"]
        self._list = []
    
    def set_contents(self, folder: Folder = "", file: File = ""):
        self._list.append(file)
        self._list.append(folder)
    
    def current_directory(self, new = ""):
        self._current_directory.append(new)
        return self._current_directory
    
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
        return f"{self._folder.current_directory()}"

    def ls(self):
        return self.get_contents()

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


sth = Folder("name")
root = Folder("new_folder", sth)
print(root.ls())





