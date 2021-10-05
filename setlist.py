import os 
import re

class Setlist():
    def __init__(self, path, f, choice, filename):
        self.path = path
        self.f = f
        self.choice = choice
        self.filename = filename
    
    def updateContents(self):
        try:
            fileInfo = open(self.filename, 'r', encoding='utf-16').readlines()
            songInfo = fileInfo[0].strip().split("\t")
            artist = songInfo.index("Artist")
            track = songInfo.index('Track Title')
            bpm = songInfo.index('BPM')

            if self.choice:
                updated_content = self.withBPM(fileInfo[1:], artist, track, bpm)
            else:
                updated_content = self.noBPM(fileInfo[1:], artist, track)

            with open("_"+self.filename,'w', encoding='utf-16') as file:
                file.write(updated_content)
            print("File updated!")

        except FileNotFoundError:
            self.fileNotFoundMessage(self.f, self.path)
            
        except IndexError:
            self.indexErrorMessage(self.f)

        except ValueError as e:
            self.valueErrorMessage(str(e[:-8]))

        close=input("press any button to exit.")

    def withBPM(self, file, artist, track, bpm):
            updated_content = ""
            for i, line in enumerate(file):
                songInfo = line.strip().split("\t")

                song = f"{i+1}. {songInfo[artist].strip()} - {songInfo[track].strip()} ({songInfo[bpm].strip()})\n"
                updated_content += song
            return updated_content

    def noBPM(self, file, artist, track):
            updated_content = ""
            for i, line in enumerate(file):
                songInfo = line.strip().split("\t")

                song = f"{i+1}. {songInfo[artist].strip()} - {songInfo[track].strip()}\n"
                updated_content += song
            return updated_content

    def fileNotFoundMessage(self, name, path):
        print("==========")
        print(f"'{name}' file not found. Did you spell it correctly?")

        print(f"Possible filenames: ")
        for file in os.listdir(path):
            if file.endswith('.txt'):
                print(f"\t• {file}")

    def indexErrorMessage(self, name):
        print("==========")
        print(f"'{name}' file format does not match Kuvo output. Did you export from Rekordbox properly?")

    def valueErrorMessage(self, val):
            print("==========")
            print(f"{val} found. Is the Artist and Track Title visible?")


def main():
    path = os.getcwd()
    f = input("Enter the name of the file: ")
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

    filename = f"{f}.txt" if f[-4:] != '.txt' else f
    setlist = Setlist(path, f, choice, filename)
    setlist.updateContents()


if __name__ == "__main__":
    main()