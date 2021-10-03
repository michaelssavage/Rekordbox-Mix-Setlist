import os 
import re

def main():
    path = os.getcwd()
    f = input("Enter the name of the file: ")

    filename = f"{f}.txt" if f[-4:] != '.txt' else f

    try:
        updated_content = ""

        for line in open(filename, 'r', encoding='utf-16'):
            songInfo = line.strip().split("\t")
            song = f"{songInfo[3].strip()} - {songInfo[4].strip()}\n"
            updated_content += song

        with open(filename,'w', encoding='utf-16') as file:
            file.write(updated_content)
        print("File updated!")

    except FileNotFoundError:
        print("==========")
        print(f"'{f}' file not found. Did you spell it correctly?")
        print(f"Possible filenames: ")
        for file in os.listdir(path):
            if file.endswith('.txt'):
                print(f"\t• {file}")
    except IndexError:
        print("==========")
        print(f"'{f}' file format does not match Kuvo output. Did you export from Rekordbox properly?")

    k=input("press any button to exit.")

if __name__ == "__main__":
    main()