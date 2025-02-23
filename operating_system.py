#new file is here
#this is the develop branch
from __future__ import annotations
python_list = []



class Folder:
    def __init__(self, file : File = "", folder : Folder = ""):
        self._file = file
        self._folder = folder
    
    def set_contents(self):
        self._list = []
        self._list.append(self._file)
        self._list.append(self.folder)
    
    def get_contents(self):
        return self._file, self._folder

    def ls(self):
        print(self.get_contents())

    def mv(self, file, destination: Folder):
        if file in self._list:
            self._list.remove(file)
            destination



class File:
    def __init__(self, file: str = ""):
        self._file = file

    @staticmethod
    def file_det():
        if self._file.endswith(".py"):
            python_list.append(self._file)






