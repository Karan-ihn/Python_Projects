import os
import shutil

path = r"D:\python\file_sorter\all_files"

files = os.listdir(path)

users = []
for file in files:
      users.append(file.lower().split("_")[0])

usernames = list(set(users))

for name in usernames:
    os.makedirs(path + "\\" + name)

for file_name in files:
    for username in usernames:
        if username in file_name.lower():
            shutil.move(path + "\\" + file_name, path + "\\" + username + "\\" + file_name)
