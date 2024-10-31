from file import File
from folder import Folder
if __name__=="__main__":
    f1=File("name.txt")
    f2=File("koushik.txt")
    dir1=Folder("Home")
    dir1.add_component(f1)
    dir1.add_component(f2)
    dir2=Folder("Parent")
    f3=File("hello.txt")
    dir2.add_component(f3)
    dir1.add_component(dir2)
    dir1.show_details()