#new file is here
#this is the develop branch
from __future__ import annotations
py = endswith(".py")


class Folder:
    def __init__(self, file : File = "", folder : Folder = ""):
        self._file = file
        self._folder = folder
    
    def get_contents(self):
        return self._file, self._folder

    def ls(self):
        self.get_contents()



class File:
    def __init__(self, python : py):
        




