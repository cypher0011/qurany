import os
import subprocess
import errno
from data import *

if not os.path.exists('quran_d'):
    os.makedirs("quran_d") 

print("""

                              
                              
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
           
------------------------------------------------
    >quran project<
    info:you can listen --- now you can listen only to mshary al-afasy 
    soon:you can download -- and listen to all readers

                """)

print("[1] mshary al-afasy")
inp=input("choose the reader:")

if inp == "1":
    soura()

print("""
        1.listen
        2.download
        3.download_all      """)

lord=input("choose:")

if lord == "1":
    sor=input("which sora:")
    number= str(sor)
    zero=number.zfill(3)
    print(zero)
    subprocess.run(["mplayer",f"https://server8.mp3quran.net/afs/{zero}.mp3"])

if lord == "2":
    sor=input("which sora:")
    number= str(sor)
    zero=number.zfill(3)
    print(zero)
    #wget https://server8.mp3quran.net/afs/114.mp3 -P /home/kali/Desktop/quran/quran_d
    #subprocess.run(["wget",f"https://server8.mp3quran.net/afs/{zero}.mp3", "-P /quran_d"])
    os.system(f"wget https://server8.mp3quran.net/afs/{zero}.mp3 -P quran_d")

if lord == "3":
    for number in range(115):
        number = str(number)
        zero=number.zfill(3)
        print(zero)
        os.system(f"wget https://server8.mp3quran.net/afs/{zero}.mp3 -P quran_d")






#import os
#os.system("ls -l")
