#!/usr/bin/env python
# coding: utf-8

# In[10]:


import os
import sys


# In[11]:


def ChangeClass (path, filename, class_name):
    f = open(os.path.join(path,filename), 'r+')
    f.truncate()
    f.write(class_name + "\n")
    f. close()
        
    


# In[17]:


def ChangeSplitPath(path, filename,class_name):
    splitTxtFile = open(os.path.join(path, filename))
    f = open("splitTrainAndTest.py", "w+")
    f.truncate()
    for line in splitTxtFile:
        if "PLACE_HOLDER_TEST" in line:
            newLine = line.replace("PLACE_HOLDER_TEST", '"' + class_name + "_test.txt" + '"')
            print(newLine)
           
        elif "PLACE_HOLDER_TRAIN" in line:
            newLine = line.replace("PLACE_HOLDER_TRAIN", '"' + class_name + "_train.txt" + '"')
            print(newLine)
        else:
            newLine = line

        f.write(newLine)
    
    
    f.close()    

def SetPathForTraining(path, filename, class_name):
    f = open("darknet.data", "w+")
    f.truncate()
    for line in open(os.path.join(path, filename)):
        if "train" in line:
            newLine = line.replace(line, "train = " + path +"/"+ class_name + "_train.txt" + "\n")
        
        elif "valid" in line:
            newLine = line.replace(line, "valid = " + path +"/"+ class_name + "_test.txt" + "\n")
        else:
            newLine = line

        f.write(newLine)
    f.close()

    
# In[12]:


basefolder = os.getcwd()
class_name = sys.argv[1]
ChangeClass(basefolder, "classes.names", class_name)
ChangeSplitPath(basefolder,"splitBlueprint.py" , class_name)
SetPathForTraining(basefolder,"darknetBlueprint.data", class_name)


# In[ ]:




