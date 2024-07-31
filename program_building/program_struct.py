import os
from tqdm import tqdm
from datetime import datetime
import time

program_name=input("Enter the program name: ")
program_path=input("Enter the program path that you want to place: ")
pbar = tqdm(total=100,leave=True)

pbar.set_description("Creating program structure")
program_place=os.path.join(program_path,program_name)
os.makedirs(program_place)
os.makedirs(os.path.join(program_place,"src"))
src_path=os.path.join(program_place,"src")
os.makedirs(os.path.join(program_place,"data"))
data_path=os.path.join(program_place,"data")
os.makedirs(os.path.join(program_place,"model"))
model_path=os.path.join(program_place,"model")
os.makedirs(os.path.join(program_place,"logs"))
logs_path=os.path.join(program_place,"logs")
os.makedirs(os.path.join(program_place,"results"))
results_path=os.path.join(program_place,"results")
os.makedirs(os.path.join(results_path,"visualization_results"))
os.makedirs(os.path.join(results_path,"calculate_result"))

os.makedirs(os.path.join(program_place,"try"))
try_path=os.path.join(program_place,"try")
with open(os.path.join(try_path,"try.ipynb"),'w') as f:
    pass
pbar.update(20)
# 创建readme.md文件
with open(os.path.join(program_place,"readme.md"),'w') as f:
    f.write("# "+program_name+" readme\n")
    f.write("This is the readme file for the program "+program_name)
    f.write("\n")
    f.write("Author: zhuzilan"+"\ncreated time:"+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"  \n\n")
    f.write("\n")
    f.write("## "+"1. Introduction\n")
    f.write("## "+"2. Data description\n")
    f.write("All the data is stored in the"+f"[data]({data_path}) folder.\n")
    f.write("Need more details? please check the"+f"[data readme]({os.path.join(data_path,'data_readme.md')}) file.\n")
    f.write("## "+"3. Model description\n")
    f.write("All the model is stored in the"+f"[model]({os.path.join(program_place,'model')}) folder.\n")
    f.write("## "+"4. Experiment results\n")
    f.write("All the results is stored in the"+f"[results]({os.path.join(program_place,'results')}) folder.\n")
    f.write("## "+"5. Using steps\n")
pbar.update(20)

with open(os.path.join(data_path,"data_readme.md"),'w') as f:
    f.write("# "+program_name+" data readme\n")
    f.write("This is the readme file for the data of the program "+program_name)
    f.write("\n")
    f.write("Author: zhuzilan"+"\ncreated time:"+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    f.write("\n")
    f.write("## "+"1. Data description\n")
    f.write("all the data is set up by the following parts:\n")
    origin_data_path=os.path.join(data_path,"origin_data")
    os.makedirs(origin_data_path)
    f.write(f"[origin_data]({origin_data_path}) folder: store the original data.\n")
    preprocessed_data_path=os.path.join(data_path,"preprocessed_data")
    os.makedirs(preprocessed_data_path)
    f.write(f"[preprocessed_data]({preprocessed_data_path}) folder: store the preprocessed data.\n")
    processed_data_path=os.path.join(data_path,"processed_data")
    os.makedirs(processed_data_path)
    f.write(f"[processed_data]({processed_data_path}) folder: store the processed data.\n")
    f.write("## "+"2. Data preprocess\n")
    f.write("data preprocess code is stored in the" + f"[data_preprocess.py]({os.path.join(src_path,'data_preprocess.py')}) file.\n")
pbar.update(10)
with open(os.path.join(src_path,"data_preprocess.py"),'w') as f:
    pass
with open(os.path.join(src_path,"main.py"),'w') as f:
    pass
with open(os.path.join(src_path,"utils.py"),'w') as f:
    pass
with open(os.path.join(src_path,"display.ipynb"),'w') as f:
    pass
pbar.update(10)

with open(os.path.join(src_path,"src_readme.md"),'w') as f:
    f.write("# "+program_name+" src readme\n")
    f.write("This is the readme file for the src of the program "+program_name)
    f.write("\n")
    f.write("Author: zhuzilan"+"\ncreated time:"+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    f.write("\n")
    f.write("## "+"1. src folder struction description\n")
    f.write("all the src is set up by the following parts:\n")
    
    f.write(f"[main.py]({os.path.join(src_path,'main.py')}) file: the main code of the program.\n")
    
    f.write(f"[utils.py]({os.path.join(src_path,'utils.py')}) file: the utils code of the program, storing the defined function.\n")

    f.write(f"[display.ipynb]({os.path.join(src_path,'display.ipynb')}) file: the display code of the program.\n")
    f.write("## "+"2. to be continue\n")
pbar.update(20)

with open(os.path.join(model_path,"model_named_readme.md"),'w') as f:
    f.write("# "+program_name+" model readme\n")
    f.write("This is the naming readme file for the model of the program "+program_name)
    f.write("\n")
    f.write("Author: zhuzilan"+"\ncreated time:"+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    f.write("\n")
    f.write("all the model need naming by the following parts:\n")
    f.write("date+try_num+train_loss+valid_loss+epoch_num\n")
    f.write("for example:\n")
    f.write("20240731_try1_trainloss0.1_validloss0.2_epoch10\n")
pbar.update(10)

with open(os.path.join(logs_path,"log_readme.md.md"),'w') as f:
    f.write("# "+program_name+" logs readme\n")
    f.write("This is the readme file for the logs of the program "+program_name)
    f.write("\n")
    f.write("Author: zhuzilan"+"\ncreated time:"+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    f.write("\n")
    f.write("logs need include loss data and figure.\n")
    f.write("all the logs need naming by the following parts:\n")
    f.write("date+try_num+train_loss+valid_loss+epoch_num\n")
    f.write("for example:\n")
    f.write("20240731_try1_trainloss0.1_validloss0.2_epoch10\n")
pbar.update(10)
pbar.close()
print("Program structure has been created successfully!")