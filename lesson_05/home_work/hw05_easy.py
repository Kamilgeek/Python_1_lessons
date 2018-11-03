__author__ = 'Магомедов Камиль Магомедович'
import os
import sys
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def ex(dirname):
    result = False
    if os.path.exists(dirname):
        result = True
    return result
 def mk(dirname):
    result = False
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        result = True
    return result
 def rm(dirname):
    result = False
    if os.path.exists(dirname):
        os.rmdir(dirname)
        result = True
    return result

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def ls( path= ".", files = False):
    res = [name for name in os.listdir( path ) if files == os.path.isfile(name)]
    return res


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copymy():
    myname = sys.argv[0]
    path, filename = os.path.split(myname)
    basename, extension = os.path.splitext(filename)
    basename = basename+"-copy"
    newfilename = path+"/"+basename+extension
    newfilename = os.path.normpath(newfilename)
    shutil.copy(myname, newfilename)
    return newfilename
 if __name__ == "__main__":
    [mk("dir_"+str(i)) for i in range(1, 10)]
    print("Создали каталоги")
    print(ls())
    [rm("dir_"+str(i)) for i in range(1, 10)]
    print("Удалили каталоги")
    print("\n")
     print(ls(".."))
    print("\n")
     print(copymy())
