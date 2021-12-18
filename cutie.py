import sys
import os
path = sys.path[4]
path = path + "\\scripts"
print(path)
os.chdir(path)
print(os.getcwd())
os.system("pip install pygame")
os.system("pip install pathfinding")

