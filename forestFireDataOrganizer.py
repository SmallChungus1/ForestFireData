import os
import shutil
import random
import glob
from PIL import Image
import sys
import forestFireFilePaths as filePaths


cwd = os.getcwd()
print(cwd)
dataPath = os.path.join(cwd, r"forestfiredatafull\Data")
os.chdir(dataPath)
print("current path", os.getcwd())
os.chdir('Train_Data/Non_Fire')
print("current path 2: ", os.getcwd())
j=0

#removing corrupted files from Trainging datasets
for i in glob.glob('NF_*'):
    try:
        img = Image.open(i)
        img.verify()
    except:
        shutil.move(i, filePaths.corruptFileCollecPath) #need to create your own py file named "filePaths", create a file to collect disposed files from the dataset, and set path to variable 'corruptFileCollecPath'
        j+=1

print("Non Fire files that are corrupted:",j)

os.chdir('../../')
print("current path 3: ", os.getcwd())
os.chdir('Train_Data/Fire')
print("current path 4: ", os.getcwd())
k = 0

for i in glob.glob('F_*'):
    
    try:
        img = Image.open(i)
        img.verify()
    except:

        shutil.move(i, filePaths.corruptFileCollecPath)
        k+=1

print("Fire files that are corrupted:",k)

FireFilesCount = len(glob.glob('F_*'))
os.chdir('../../')
os.chdir('Train_Data/Non_Fire')
NFireFilesCount = len(glob.glob('NF_*'))
os.chdir('../../')

print ("total fire files:", FireFilesCount)


if FireFilesCount > NFireFilesCount:
    BalanceFireNoFire = FireFilesCount - NFireFilesCount
    print("count: ", BalanceFireNoFire)
    os.chdir('Train_Data/Fire')
    for i in random.sample(glob.glob('F_*'), BalanceFireNoFire):
        shutil.move(i, filePaths.corruptFileCollecPath)
    FireFilesCount = len(glob.glob('F_*'))

else:
    BalanceFireNoFire = NFireFilesCount - FireFilesCount
    print("count: ", BalanceFireNoFire)
    os.chdir('Train_Data/Non_Fire')
    for i in random.sample(glob.glob('NF_*'), BalanceFireNoFire):
        shutil.move(i, filePaths.corruptFileCollecPath)
    NFireFilesCount = len(glob.glob('NF_*'))

validSetSize = int(FireFilesCount*0.1) #set valid set size as 10% of fire train set after fire train set is balanced with non fire train set
print("valid Set Size: ", validSetSize)
os.chdir('../../')
print("current path 5:", os.getcwd())

if os.path.isdir('Valid_Data/Non_Fire') is False:
    os.makedirs('Valid_Data/Non_Fire')
    os.makedirs('Valid_Data/Fire')

    print("current path 6:", os.getcwd())

    #shuffle Fire and Non Fire training sets, balance two sets
    # os.chdir('Train_Data/Non_Fire')
    # #moving part of train data into valid set
    # nf_Files = glob.glob('NF_*')
    # os.chdir('../../')
    # for i in random.sample(nf_Files, validSetSize): #10% of train set
    #     shutil.move(i, 'Valid_Data/Non_Fire')
    
    # os.chdir('Train_Data/Fire')
    # nf_Files = glob.glob('F_*')
    # os.chdir('../../')
    # for i in random.sample(glob.glob('F_*.jpg'), validSetSize):
    #     shutil.move(i, 'Valid_Data/Fire')  
#os.chdir('../../')
print("current working directory after dataset manipulation:", os.getcwd())

