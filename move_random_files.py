import os
import random
import shutil
import math

source = r'Z:\Alex P\Bao\Pass_11_02_Trimmed'
dest = r'Z:\Alex P\Bao\LMIS ML\data'
files = os.listdir(source)
train = 648 #math.floor(len(files)*.70)
valid = 185 #math.floor(len(files)*.20)
mode = "pass"
for file_name in random.sample(files, train):
    train_dest = f"{dest}\\train\\{mode}"
    shutil.move(os.path.join(source, file_name), train_dest)

files = os.listdir(source)

for file_name in random.sample(files, valid):

    valid_dest = f"{dest}\\valid\\{mode}"
    shutil.move(os.path.join(source, file_name), valid_dest)

files = os.listdir(source)

for file_name in random.sample(files,93):
    test_dest = f"{dest}\\test\\{mode}"
    shutil.move(os.path.join(source, file_name), test_dest)