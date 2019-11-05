import os

#print(dir(os))

#print(os.getcwd())

os.chdir('/Users/tglen/Desktop')

#print(os.listdir())

## to create folder 
# make single directory
os.mkdir('made_python')
# make dir & sub dir (multiple directories)
# can create an entire tree with one function
os.makedirs('made_python/python_subDir')

#remove the sub directory
os.rmdir('made_python/python_subDir')

# add the sub DIr back

os.makedirs('made_python/python_subDir2')

#check to see fi new Dir was made.
 print(os.listdir())

 #rename takes two params first is file to change second is new name
 #make sure your in correct dir to rename. pwd for this code its ../Desktop/made_python/python_subDir2/test.txt
 os.rename('test.txt', 'test_rename.txt')

 # os.stat to get file size
 #stat should info including time, size, etc..
 #when lookign at time use datetime libary to make it human readable

print(os.stat('test_rename.txt').st_size) # should return file size.

#os.walk() example. This will step through my desktop printing all the file and directory info


for dirpath, dirnames, filenames in os.walk('/Users/tglen/Desktop'):
    print('Current path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()
