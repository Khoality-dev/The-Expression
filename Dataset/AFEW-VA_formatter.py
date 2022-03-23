import json
import os
import shutil
import pandas as pd
from alive_progress import alive_bar

if __name__ == "__main__":
    data_dir = "AFEW-VA"
    target_dir = "src_data"

    os.makedirs(target_dir, exist_ok = True)

    arousals = []
    new_file_names = []
    valences = []

    folders = [f for f in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, f))]
    print("Formating file structure...")
    with alive_bar(len(folders)) as bar:
        for folder_name in folders:
            #print("/"+folder_name+"/...")
            files = [f for f in os.listdir(os.path.join(data_dir,folder_name)) if os.path.isfile(os.path.join(os.path.join(data_dir,folder_name), f))]
            for file_name in files:
                if os.path.splitext(file_name)[1] == ".png":
                    if (not(os.path.exists(os.path.join(target_dir, folder_name+"_"+file_name)))):
                        shutil.move(os.path.join(os.path.join(data_dir, folder_name), file_name), os.path.join(target_dir, folder_name+"_"+file_name))
            
            #label formating
            with open(os.path.join(os.path.join(data_dir, folder_name), folder_name+ ".json")) as jsonFile:
                jsonData = json.load(jsonFile)['frames']
                for frame in jsonData:
                    new_file_names.append(folder_name + "_" + frame + ".png")
                    arousals.append(jsonData[frame]['arousal'])
                    valences.append(jsonData[frame]['valence'])
            bar()
    print("Done!")
    
    dict = {'file_name': new_file_names, 'arousal': arousals, 'valence': valences}
    pd.DataFrame(dict).to_csv(os.path.join(target_dir, "label_data.csv"), index=False)