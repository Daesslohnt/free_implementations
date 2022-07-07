import os

# get current working directory
cwd = os.getcwd()

# change directory
os.chdir("..")

# create a new empty directory
empty_directory = "test_dir"
path = os.path.join(cwd, empty_directory)
os.mkdir(path)

# create create empty file in the new empty directory
empty_file = "test_file.txt"
new_empty_file = "file_text.txt"
file_path = os.path.join(cwd, empty_directory, empty_file)
new_file_path = os.path.join(cwd, empty_directory, new_empty_file)
with open(file_path, 'w') as f:
    pass

# check the existence of empty file, rename it and delete
if os.path.exists(file_path):
    print('Size of file: ', os.path.getsize(file_path))
    os.rename(file_path, new_file_path)
    os.remove(new_file_path)

# remove empty directory
os.rmdir(path)

# list all files and directories in saved path
dir_list = os.listdir(cwd)
print('list of all files and dirs in {}:'.format(cwd), dir_list)