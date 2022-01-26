
import os
import random
import shutil
import zipfile
from conf import Config
backslash = "\\"


def debug():
    for (dirpath, dirnames, filenames) in os.walk("./"):
        print("\n\n\n\n\n")
        print("DIRPATH: " + dirpath)
        print("\n\n\n*************************************\n\n\n")
        print("DIRNAMES: ")
        print(dirnames)
        print("\n\n\n*************************************\n\n\n")
        print("FILENAMES: ")
        print(filenames)
        print("\n\n\n\n\n FINISH\n\n\n\n\n\n\n\n")

# dirpath direkt her şeyi veriyor
if not os.path.isdir('randomTextures'):
    os.mkdir('randomTextures')

# def randomize_textures():
#     for (dirpath, dirnames, filenames) in os.walk("./assets/minecraft/textures"):
#         print(f"\n\n\n\n{dirpath} Hallediliyor\n\n\n\n")
#         a = 0
#         olddirlist = []
#         for i in filenames:
#             old_name = os.path.join(dirpath, i)
#             olddirlist.append(old_name)
#         for i in filenames:
#             oldname = random.choice(olddirlist).replace(backslash, "/")
#             newname = (os.path.join(dirpath, i).replace(backslash, '/'))
#             print(f"\n\nESKI AD: {oldname}\nYENI AD: {newname}\n\n")
            
newdir = 'randomTextures'
zipname = 'random.zip'
mindfuck = ['./assets\minecraft\\blockstates', './assets\minecraft\\font',
                    './assets\minecraft\lang', './assets\minecraft\shaders', './assets\minecraft\shaders\core',
                    './assets\minecraft\shaders\include', './assets\minecraft\shaders\post', './assets\minecraft\shaders\program',
                    './assets\minecraft\\texts', './assets\minecraft\particles', './assets\minecraft\models'
                    ]     

medium = ['./assets\minecraft\\blockstates', './assets\minecraft\\font',
                    './assets\minecraft\lang', './assets\minecraft\shaders', './assets\minecraft\shaders\core',
                    './assets\minecraft\shaders\include', './assets\minecraft\shaders\post', './assets\minecraft\shaders\program',
                    './assets\minecraft\\texts', './assets\minecraft\particles', './assets\minecraft\models', './assets\minecraft\\textures\\font',
                    './assets\minecraft\\textures\gui']

forbidden_files = medium
def randomize():
    if os.path.exists('./' + zipname):
        print('Undeleted files found, deleting...')
        os.remove('./' + zipname)
    if os.path.exists('./randomTextures'):
        shutil.rmtree('./randomTextures')
    print('Randomizing Textures')
    for (dirpath, dirnames, filenames) in os.walk('./assets'):
        if dirpath in forbidden_files:
            print(f"{dirpath} IS PASSED")
            continue
        olddirlist = []
        with open('sj.txt', 'a', encoding='utf-8') as file:
            file.write(f"\n\n\n\n{dirpath} Hallediliyor\n\n\n\n")
        a = 0
        newdirpath ='./' + newdir + dirpath.strip('.')
        os.makedirs(newdirpath)
        for i in filenames:
            old_name = os.path.join(dirpath, i)
            olddirlist.append(old_name)
        for i in filenames:
            oldname = random.choice(olddirlist).replace(backslash, "/")
            newname = (os.path.join(newdirpath, i).replace(backslash, '/'))
            shutil.copyfile(oldname, newname)
            # print(F'\n\nESKI AD: {oldname}\nYENI AD: {newname}\n\n')

def create_pack():
    print('Creating texture pack')
    forbiddenKeywords = ['__pycache__','conf.py', 'randomTextures', 'randomize_textures.py', 'assets', '.git', '.gitignore', 'README.md']
    forbiddenzipwords = ['__pycache__', 'conf.py','randomTextures', 'randomize_textures.py', '.git', '.gitignore', 'README.md']
    for i in os.listdir('.'):
        if i not in forbiddenKeywords:
            shutil.copyfile(os.path.join('.', i), os.path.join('./' + newdir, i))
    newzip = zipfile.ZipFile('./' + zipname , 'w')
    for (dirpath, dirname, filenames) in os.walk('./' + newdir):
        if dirpath not in forbiddenzipwords:

            for i in filenames:
                copyfile = os.path.join(dirpath, i)
                copyname = copyfile[(len(newdir) + 3)::].strip('..')
                # print(f"writing {copyfile} to zip file as {copyname}")
                newzip.write(copyfile, copyname)


def copy_file_to_resource_folder():
    if Config.resource_location:
        try:
            resloc = str(Config.resource_location).strip("b'").rstrip("'")
            print(f"Resource location found...\nCopying to {resloc}")
            if os.path.exists(resloc + '/' + zipname):
                print('Undeleted zip in texture folder found, deleting...')
                os.remove(os.path.join(resloc, zipname))
                print(os.path.join(resloc, zipname) + ' was deleted')
            shutil.copyfile(zipname, resloc + '/' + zipname)
            print('Copied new file to resource directory')
        except FileNotFoundError:
            print('You forgot to change your config file or your file path was invalid.\nYour file is ready at the root folder!')
    else:
        print('No resource location found. Your file is ready at the root folder!')


if __name__ == "__main__":
    randomize()
    create_pack()
    copy_file_to_resource_folder()
    