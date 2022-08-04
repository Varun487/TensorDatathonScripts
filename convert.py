from os import listdir
from os.path import isfile, isdir, join
import os
import pandas as pd

main_dir = r"C:\Users\seshu\Documents\college_everything\SEM4\TENSOR_STUFF\DATASETS\NEW\SOUTH_CAROLINA"

for path, folder, files in list(os.walk(main_dir)):
    files = [join(path,file) for file in files]
    if files and files[0].endswith(".txt"):
        print(files[0])
        try:
            df = pd.read_csv(files[0], delimiter="\s+", low_memory=False)
            df.to_csv(join(r"C:\Users\seshu\Documents\college_everything\SEM4\TENSOR_STUFF\DATASETS\NEW\CSVS",(files[0].split("\\")[12].split(".")[0] + ".csv")))

        except:
            print("DIDN'T work for " + files[0])