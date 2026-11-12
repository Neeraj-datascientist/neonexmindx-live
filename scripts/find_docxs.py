import os
import glob
import re

print("Looking in c:/Users/pcnee/Downloads:")
for f in glob.glob("c:/Users/pcnee/Downloads/*Data*Science*"):
    print(" ", f)

print("Looking in c:/Users/pcnee/Desktop/NeoNeX MindX website:")
for f in glob.glob("c:/Users/pcnee/Desktop/NeoNeX MindX website/**/*Data*Science*", recursive=True):
    print(" ", f)

