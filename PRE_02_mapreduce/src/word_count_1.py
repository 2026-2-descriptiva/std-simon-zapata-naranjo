import glob
import os.path
import string
import time

#global variables
DATA_FOLDER="PRE_02_mapreduce/data"
INPUT_FOLDER="PRE_02_mapreduce/temp/input"
OUTPUT_FOLDER="PRE_02_mapreduce/temp/output"
#n variable copies of the input files to create
n=1000

#create a temporary folder to store the input and outpu files
#and create multiple input files with the content of the original files 

#empty the input and output folders
if os.path.exists(INPUT_FOLDER):
    for file in glob.glob(INPUT_FOLDER + "/*"):
        os.remove(file)
else:
    os.makedirs(INPUT_FOLDER)

if os.path.exists(OUTPUT_FOLDER):
    for file in glob.glob(OUTPUT_FOLDER + "/*"):
        os.remove(file)
else:
    os.makedirs(OUTPUT_FOLDER)

#generate n copies of the input files
for file in glob.glob(f"{DATA_FOLDER}/*"):
    with open(file,"r", encoding="utf-8") as f:
        text=f.read()
    for i in range(1,n+1):
        raw_filename_w_e=os.path.basename(file)
        raw_filename_wo_e=os.path.splitext(raw_filename_w_e)[0]
        new_filename=f"{raw_filename_wo_e}_{i:05d}.txt"
        with open(f"{INPUT_FOLDER}/{new_filename}","w",encoding="utf-8") as f2:
            f2.write(text)

# read files
start_time = time.time()
sequence=[]
files=glob.glob(f"{INPUT_FOLDER}/*")
for file in files:
    with open(file,"r",encoding="utf-8") as f:
        for line in f:
            sequence.append((file,line))


#implement the mapreduce algorithm
#map phase
pairs_sequence=[]
for _,line in sequence:
    line=line.lower()
    line=line.translate(str.maketrans("","",string.punctuation))
    line=line.replace("\n","")
    words=line.split()
    pairs_sequence.extend([word,1] for word in words)


#shuffle and sort phase
pairs_sequence=sorted(pairs_sequence)

#reduce phase
result=[]
for key,value in pairs_sequence:
    if result and result[-1][0]==key:
        result[-1]=(key, result[-1][1]+value)
    else:
        result.append([key,value])

#write the result
with open(f"{OUTPUT_FOLDER}/part-00000","w",encoding="utf-8") as f:
    for key,value in result:
        f.write(f"{key} {value}\n")
    f.close()

#success file
with open(f"{OUTPUT_FOLDER}/_SUCCESS","w",encoding="utf-8") as f:
    f.write("")
    f.close()

#time taken
end_time = time.time()
print(f"Execution time: {end_time - start_time:.2f} seconds")