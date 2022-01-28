
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

            
newdir = 'randomTextures'
zipname = 'random.zip'
mindfuck = ['./default/assets\minecraft\\blockstates', './default/assets\minecraft\\font',
                    './default/assets\minecraft\lang', './default/assets\minecraft\shaders', './default/assets\minecraft\shaders\core',
                    './default/assets\minecraft\shaders\include', './default/assets\minecraft\shaders\post', './default/assets\minecraft\shaders\program',
                    './default/assets\minecraft\\texts', './default/assets\minecraft\particles', './assets\minecraft\models'
                    ]     

medium = ['./default/assets\minecraft\\blockstates', './default/assets\minecraft\\font',
                    './default/assets\minecraft\lang', './default/assets\minecraft\shaders', './default/assets\minecraft\shaders\core',
                    './default/assets\minecraft\shaders\include', './default/assets\minecraft\shaders\post', './default/assets\minecraft\shaders\program',
                    './default/assets\minecraft\\texts', './default/assets\minecraft\particles', './default/assets\minecraft\models', './default/assets\minecraft\\textures\\font',
                    './default/assets\minecraft\\textures\gui']

forbidden_files = medium

def check_compability():
    resource_location = b"your/path\\here\\put\\double\\backslashes"
    if Config.resource_location == resource_location:
        print("You haven't changed your resource location from ./conf.py! Your pack will only be saved to the out folder...")
    if os.path.exists('./out/' + zipname):
        print('Undeleted files found, deleting...')
        os.remove('./out/' + zipname)
    if os.path.exists('./out/randomTextures'):
        shutil.rmtree('./out/randomTextures')
    if not os.path.exists('./out'):
        print('Creating out folder...')
        os.mkdir('./out')

def randomize():

    print('Randomizing Textures')
    for (dirpath, dirnames, filenames) in os.walk('./default/default/assets/'):
        if dirpath in forbidden_files:
            print(f"{dirpath} IS PASSED")
            continue
        olddirlist = []
        newdirpath ='./out/' + newdir + dirpath.strip('.').replace('default/', '')
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
    allowedKeywords = ['pack.mcmeta', 'pack.png']
    allowedZipWords = ['pack.mcmeta', 'pack.png']
    for i in os.listdir('./default'):
        if i in allowedKeywords:
            shutil.copyfile(os.path.join('./default', i), os.path.join('./out/' + newdir, i))
    newzip = zipfile.ZipFile('./out/' + zipname , 'w')
    for (dirpath, dirname, filenames) in os.walk('./out/'):
        
        for i in filenames:
            copyfile = os.path.join(dirpath, i)
            copyname = copyfile[(len(newdir) + 7)::].strip('..')
            newzip.write(copyfile, copyname)


def copy_file_to_resource_folder():
    try:

        resloc = str(Config.resource_location).strip("b'").rstrip("'")
        print(f"Resource location found...\nTrying to copy file to {resloc}")
        if os.path.exists(resloc + '/' + zipname):
            print('Undeleted zip in texture folder found, deleting...')
            os.remove(os.path.join(resloc, zipname))
            print(os.path.join(resloc, zipname) + ' was deleted')
        shutil.copyfile('./out/' + zipname, resloc + '/' + zipname)
        print('Copied new file to resource directory')

    except FileNotFoundError:
        print("You haven't specified your resourcepack folder or it was invalid!\nYour file is ready at the out folder!")

    except:
        print("Something went wrong! please contact me with the error bellow")
        raise

def main():
    check_compability()
    randomize()
    create_pack()
    copy_file_to_resource_folder()
    

if __name__ == "__main__":
    main()