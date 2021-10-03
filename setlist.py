import os 
import re

directory = r"C:\Users\micha\Documents\Mixes"
f = input("Enter the name of the file: ")

if f[-4:] != '.txt':
    filename = f"{f}.txt"

if os.getcwd() != directory:
    os.chdir(directory)

try:
    updated_content =""

    for line in open(filename, 'r', encoding='utf-16'):
        songInfo = line.strip().split("\t")
        song = f"{songInfo[3].strip()} - {songInfo[4].strip()}\n"
        updated_content += song

    with open(filename,'w', encoding='utf-16') as file:
        file.write(updated_content)
    
    print("File updated!")
except FileNotFoundError:
    print("==========")
    print(f"File not found: {f}. Did you spell it correctly?")
    print(f"Possible filenames: ")
    for i,file in enumerate(os.listdir(directory)):
        if file.endswith('.txt'):
            print(f"\t{i+1}. {file}")

k=input("press any buton to exit")
