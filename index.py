#%%
import os 
import shutil

file1 = input("enter the file Name to replace")
file2 = input("Enter the Fake File Name to add")

file1 = file1 + "/"
file2 = file2 + "/"

list_of_files = os.listdir(file1)

for file in list_of_files:
    shutil.move((file1+file),file2)
  

# %%
