# from os import listdir
# from os.path import isfile, join 
# from collections import deque

# def printnames(start_dir):
#     #we use queue to keep track of folders to search
#     search_queue = deque()
#     search_queue.append(start_dir)
#     #while queue is not empty, pop off a folder to look through
#     while search_queue:
#         dir = search_queue.popleft()
#         # loop through every file and folder in this folder
#         for file in sorted(listdir(dir)):
#             fullpath = join(dir, file)
#             if isfile(fullpath):
#                 #if it is a file print ot the full name
#                 print(file)
#             else:
#                 #if it is a folder, add it to the queue of folders to search
#                 search_queue.append(fullpath)

# printnames("pics")


# recursive directory search
from os import listdir
from os.path import isfile, join

def printnames(dir):
    # loop through every file and folder in the current folder
    for file in sorted(listdir(dir)):
        fullpath = join(dir, file)
        if isfile(fullpath):
            #if it is a file, print out the name
            print(file)
        else:
            #if it is a folder, call this function recursively on it
            #to look for files and folders
            printnames(fullpath)

printnames("pics")