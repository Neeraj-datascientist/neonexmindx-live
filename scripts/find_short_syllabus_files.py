import os
import glob

print("Looking for short course syllabus files in syllabus/:")
for f in glob.glob('deployment_NeoNex/syllabus/**/*', recursive=True):
    if any(k in f.lower() for k in ['sql', 'python', 'excel', 'tableau', 'power_bi', 'machine_learning', 'ml']):
        print(" ", f)

print("\nLooking in downloads:")
for f in glob.glob('c:/Users/pcnee/Downloads/*'):
    if any(k in f.lower() for k in ['sql', 'python', 'tableau', 'excel', 'machine learning', 'syllabus']):
        print(" ", f)
