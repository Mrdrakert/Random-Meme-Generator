from PIL import Image
import os
import random
import configparser
#from functions import setup, check_config, open_rand_img, open_rand_temp, check_current, modify_the_image, save_image, increase_config

def setup():
    if not os.path.isfile('config.ini'):
        config['FILE NAME'] = {'currentfilename': '0'}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

def open_rand_img():
    randomfile = random.choice(os.listdir(shitimages))
    while not randomfile.endswith('.png'):
            randomfile = random.choice(os.listdir(shitimages))
    return Image.open(os.path.join(shitimages, randomfile))

def open_rand_temp():
    randomfile = random.choice(os.listdir(templatedir))
    while not randomfile.endswith('.png'):
            randomfile = random.choice(os.listdir(templatedir))
    return Image.open(os.path.join(templatedir, randomfile))

def check_config():
    config.read('config.ini')
    conffirst = temp.filename.rstrip('.png')
    return config[conffirst[-4:]]['imagescount']

def check_current(number):
    global pastex1
    global pastey1
    global pastex2
    global pastey2
    config.read('config.ini')
    conffirst = temp.filename.rstrip('.png')
    conffirst = conffirst[-4:]
    pastex1 = config[conffirst][str(number)+"x1"]
    pastey1 = config[conffirst][str(number)+"y1"]
    pastex2 = config[conffirst][str(number)+"x2"]
    pastey2 = config[conffirst][str(number)+"y2"]

def modify_the_image(randimg,x1,y1,x2,y2):
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    offset = (x1, y1)
    temp.paste(randimg.resize((x2-x1, y2-y1), Image.BICUBIC), offset)



def save_image():
    global curname
    config.read('config.ini')
    curname = int(config['FILE NAME']['currentfilename'])
    temp.save(memesdir+'/meme_'+str(curname)+'.png')


def increase_config():
    global curname
    curname += 1
    config.set('FILE NAME', 'currentfilename', str(curname))
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

shitimages = os.path.join(os.path.dirname(__file__), "1. Images")
templatedir = os.path.join(os.path.dirname(__file__), '2. Templates')
memesdir = os.path.join(os.path.dirname(__file__), "3. Memes made (output)")

pastex1 = 0
pastey1 = 0
pastex2 = 0
pastey2 = 0

config = configparser.ConfigParser()
setup()
temp = open_rand_temp()
check_config()
for i in range(0, int(check_config())):
    check_current(i+1)
    modify_the_image(open_rand_img(),pastex1,pastey1,pastex2,pastey2)

curname = 0
save_image()
increase_config()
