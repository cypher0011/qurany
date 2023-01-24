import os
from re import search , MULTILINE
import subprocess
import distro
from data import soura


# colors
nocolor = "\033[0m"
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
white = "\033[0;37m"

# check the distribution name
with open("/etc/os-release") as f:
        contents = f.read()
        
match = search(r"^ID_LIKE=(.*)$", contents, MULTILINE)
if match:
    distribution = match.group(1).strip('"')
    # check if mplayer is installed
    if os.path.exists('/usr/bin/mplayer') == False:
        if distribution == "arch":
            subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "mplayer"])
        elif distribution == "alpine":
            subprocess.run(["sudo", "apk", "add", "mplayer"])
        else:
            subprocess.run(["sudo", "apt-get", "install", "-y", "mplayer"])    


os.system("clear")
if not os.path.exists("downloads"):
    os.makedirs("downloads")

print(
    """

                              
                              
   __ _ _   _ _ __ __ _ _ __  
  / _` | | | | '__/ _` | '_ \ 
 | (_| | |_| | | | (_| | | | |
  \__, |\__,_|_|  \__,_|_| |_|
     | |                      
     |_|                      

               ,   ,  
              /////|
             ///// |
            /////  |
           |~~~|   |
           |===|   |
           | q |   |
           | u |   |
           | r |   |
           | a |  /
           | n | /
           |===|/
           '---'  
           
     ~quran project~
    
    (this project is waqf for allah)

    update: you can listen to some of famous shaiks 
    comming: listen to all shaiks - can open quran from terminal - add the arabic language
                """
)
print(
    f"""
        1.listen
        2.download
        3.download_all      \n\n\n"""
)
try:
    first_menu = input(">> ")
    if first_menu == "1":
        os.system("clear")
        print("      readers name\n\n")
        print("[+]top readers:")
        print("[1] mashary al-afasy [2] maher al muaiqly [3] yaser aldossary \n\n\n")
        inp = input("choose the reader:")

        if inp == "1":
            os.system("clear")
            soura()
            sora = input(">>")
            number = str(sora)
            zero = number.zfill(3)
            print(zero)
            subprocess.run(["mplayer", f"https://server8.mp3quran.net/afs/{zero}.mp3"])
        if inp == "2":
            os.system("clear")
            soura()
            sora = input(">>")
            number = str(sora)
            zero = number.zfill(3)
            print(zero)
            subprocess.run(
                ["mplayer", f"https://server8.mp3quran.net/maher/{zero}.mp3"]
            )

        if inp == "3":
            os.system("clear")
            soura()
            sora = input(">>")
            number = str(sora)
            zero = number.zfill(3)
            print(zero)
            subprocess.run(
                ["mplayer", f"https://server11.mp3quran.net/yasser/{zero}.mp3"]
            )

    if first_menu == "2":
        os.system("clear")
        print("\t\t\t[+]download")
        soura()
        sor = input("which sora:")
        number = str(sor)
        zero = number.zfill(3)
        print(zero)
        # wget https://server8.mp3quran.net/afs/114.mp3 -P /home/kali/Desktop/quran/downloads
        # subprocess.run(["wget",f"https://server8.mp3quran.net/afs/{zero}.mp3", "-P /downloads"])
        os.system(f"wget https://server8.mp3quran.net/afs/{zero}.mp3 -P downloads")

    if first_menu == "3":
        for number in range(115):
            number = str(number)
            zero = number.zfill(3)
            print(zero)
            os.system(f"wget https://server7.mp3quran.net/afs/{zero}.mp3 -P downloads")


except KeyboardInterrupt:
    os.system("clear")
    print("👋"+" السلام عليكم الرحمة الله وبركاته"+"في امان الله")
    exit(0)

    # import os
    # os.system("ls -l")
