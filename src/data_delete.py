import os
import shutil

base_path = "/data/protein/CAMEO/data/"

allDelDir_list = ["hhblist_bfd_ucl_aln", "hhblist_bfd_ucl_fa", 
               "jackhmmer_bfd_fa", "jackhmmer_bfd_sto", 
               "jackhmmer_mgnify_fa", "jackhmmer_mgnify_sto"]

partDeldir_list = ["jackhmmer_bfd_a3m", "jackhmmer_mgnify_a3m", "hhblist_bfd_ucl_a3m"]

dataDirs = os.listdir(base_path)

for dataDir in dataDirs:
    one_week_dir = os.path.join(base_path, dataDir)
    del_base_path = os.path.join(one_week_dir, "search")
    for allDelDir in allDelDir_list:
        oneDelDir = os.path.join(del_base_path, allDelDir)
        
        # delete dir in allDelDir_list
        if os.path.exists(oneDelDir):
            print("one delete dir: ", oneDelDir)
            try:
                shutil.rmtree(oneDelDir)
            except PermissionError as e:
                        continue
    
    for partDeldir in partDeldir_list:
        onePartDelDir = os.path.join(del_base_path, partDeldir)
        
        if os.path.exists(onePartDelDir):
            print("one part delete dir: ", onePartDelDir)
            delFiles = os.listdir(onePartDelDir)
            for delFile in delFiles:
                if "@" in delFile:
                    delAm3File = os.path.join(onePartDelDir, delFile)
                    # delete file like "2023-12-30_00000013_3_127@s@0@e@355.a3m"
                    try:
                        os.remove(delAm3File)
                    except PermissionError as e:
                        continue
    # break

