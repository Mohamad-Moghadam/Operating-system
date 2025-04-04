#new file is here
#this is the develop branch
from __future__ import annotations
from abc import ABC
from typing import Optional


class Tree(ABC):
    def __init__(self, previous_node: Optional[str], current: str, next_node: str):
        self._previous= previous_node
        self._current= current
        self._next= next_node


class Commands(Tree):
    def __init__(self, previous_node: Optional[str], current: str, next_node: Optional[str]):
        super().__init__(previous_node, current, next_node)
        self._list = []

    def mkdir(self, folder_name: Root):
        self._path= self._current
        self._new_folder= folder_name

    def cd(self, destination):
        self._destination = destination
        if self._destination in self._list:
            self._folder.current_directory()
        else:
            raise FileNotFoundError()

    def rm(self, folder: str):
        self._list= self._list.remove(folder)

class Root(ABC):
    def __init__(self, name: str, folder : Root = None, file : File = None):
        self._name = name
        self._folder = folder if folder is not None else self
        self._first_directory = ["~"]
        self._list = []

    def set_contents(self, folder: Root = "", file: File = ""):
        self._list.append(file)
        self._list.append(folder)

    def current_directory(self, new = ""):
        self._current_directory.append(new)
        return self._current_directory

    def mkdir(self, folder_name: Root):
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

    def mv(self, file, destination: Root):
        if file in self._list:
            self.set_contents(file)


class Folder(Root):
    def __init__(self, name, folder, file):
        super().__init__(name : str, folder : Root = None, file : File = None)

    def set_contents(self, folder: Root = "", file: File = ""):
        super().set_contents(folder, file)



class File:
    def __init__(self, file: str = ""):
        self._file = file

    @staticmethod
    def file_det():
        if self._file.endswith(".py"):
            python_list.append(self._file)


sth = Root("name")
root = Root("new_folder", sth)
print(root.ls())





