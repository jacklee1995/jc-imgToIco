import os
import datetime
from PIL import Image
from utils import get_allfiles_path
from const import SOURCES_DIR, OUTPUT_DIR, CONFIG_file_path
from config import read_ini_as_dict

def get_now():
    now=datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def is_png_file(file_path)->bool: return (os.path.splitext(os.path.basename(file_path))[-1]).lower()==".png"

def is_jpg_file(file_path)->bool: return (os.path.splitext(os.path.basename(file_path))[-1]).lower()==".jpg"

def save_as_ico(png_path, ico_path, size=(256,256)):
    ico_path_outputs = ico_path+"_"+str(size[0])+"x"+str(size[1])+".ico"
    im = Image.open(png_path).resize(size)
    try:
        im.save(ico_path_outputs)
        print('['+get_now()+"] [INFO] [OK] File "+png_path+" has saved as "+ico_path_outputs)
    except Exception as e:
        print('['+get_now()+'] [ERROR] Can\'t convert image:',file)
        print(e)

if __name__ == "__main__":
    sources = get_allfiles_path(SOURCES_DIR)
    print('['+get_now()+"] [INFO] Reading confs...")
    conf_dict = read_ini_as_dict(CONFIG_file_path)
    sz = conf_dict['convert']['output_size'].split("x")
    size = (int(sz[0]),int(sz[1]))
    for file in sources:
        if is_png_file(file):
            print('['+get_now()+"] [INFO] Convertting .png file \""+file+"\" into .ini file, please wait...")
            _ = os.path.join(OUTPUT_DIR,os.path.basename(file)).split(".")
            output_name = ""
            if len(_)==2:
                output_name = _[0]
            else:
                for i in range(len(_)-1):
                    output_name = output_name + "_" + _[i]
            save_as_ico(file,output_name,size)

        else:
            print('['+get_now()+'] [ERROR] This is not a .png file')
