import os 
import re

def getBPMChoice():
    loop = True
    choice = False
    while loop:
        c = input("Do you want to include the BPM? enter Y or N: ")
        if c.upper() == "Y":
            choice = True
            loop = False
        elif c.upper() == "N":
            loop = False
        else:
            print("Please enter Y or N only.")
    return choice

def main():
    path = os.getcwd()
    f = input("Enter the name of the file: ")

    choice = getBPMChoice()
    filename = f"{f}.txt" if f[-4:] != '.txt' else f

    try:
        updated_content = ""

        fileInfo = open(filename, 'r', encoding='utf-16').readlines()
        songInfo = fileInfo[0].strip().split("\t")
        artist = songInfo.index("Artist")
        track = songInfo.index('Track Title')
        bpm = songInfo.index('BPM')

        for i, line in enumerate(fileInfo[1:]):
            songInfo = line.strip().split("\t")

            song = f"{i+1}. {songInfo[artist].strip()} - {songInfo[track].strip()}\n"
            if choice:
                song = song[:-2] + f" ({songInfo[bpm].strip()})\n"

            updated_content += song

        with open("_"+filename,'w', encoding='utf-16') as file:
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
    except ValueError as e:
        print("==========")
        print(f"{str(e)[:-8]} found. Is the Artist and Track Title visible?")

    k=input("press any button to exit.")

if __name__ == "__main__":
    main()