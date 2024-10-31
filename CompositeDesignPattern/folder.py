from filesystemcomponent import FileSystemComponent
class Folder(FileSystemComponent):
    def __init__(self,name):
        self.name=name
        self.components=[]
    def add_component(self, component):
        self.components.append(component)
    def remove_component(self, componet):
        self.components.remove(componet)
    def show_details(self):
        print(f"Folder name: {self.name}")
        for component in self.components:
            component.show_details()
    