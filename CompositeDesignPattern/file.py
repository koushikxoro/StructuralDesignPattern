from filesystemcomponent import FileSystemComponent
class File(FileSystemComponent):
    def __init__(self,name):
        self.name=name
    def show_details(self):
        print(f"Name of file:{self.name}")