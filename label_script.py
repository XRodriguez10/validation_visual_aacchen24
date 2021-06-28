import os
root = './val_label/'
for f in os.listdir(root):
    #print(f)
    #print(type(f))
    if 'color' not in f:
        os.remove(root+f)
    #break
