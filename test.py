import os
import subprocess
import errno

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

print("afs:mshary al-afasy")
print("choose:")
inp=input("choose the reader:")

if inp == "afs":
    print("""
1. Al-Fatihah 
2. Al-Baqarah 
3. Aali Imran 
4. An-Nisa 
5. Al-Maidah 
6. Al-Anam 
7. Al-Araf 
8. Al-Anfal 
9. At-Taubah 
10. Yunus 
11. Hud 
12. Yusuf 
13. Ar-Rad 
14. Ibrahim 
15. Al-Hijr 
16. An-Nahl 
17. Al-Isra 
18. Al-Kahf 
19. Maryam 
20. Ta-Ha 
21. Al-Anbiya 
22. Al-Haj 
23. Al-Muminun 
24. An-Nur 
25. Al-Furqan 
26. Ash-Shuara 
27. An-Naml 
28. Al-Qasas 
29. Al-Ankabut 
30. Ar-Rum 
31. Luqman 
32. As-Sajdah 
33. Al-Ahzab 
34. Saba 
35. Al-Fatir 
36. Ya-Sin 
37. As-Saffah 
38. Sad 
39. Az-Zumar 
40. Ghafar 
41. Fusilat 
42. Ash-Shura 
43. Az-Zukhruf 
44. Ad-Dukhan 
45. Al-Jathiyah 
46. Al-Ahqaf 
47. Muhammad 
48. Al-Fath 
49. Al-Hujurat 
50. Qaf 
51. Adz-Dzariyah 
52. At-Tur 
53. An-Najm 
54. Al-Qamar 
55. Ar-Rahman 
56. Al-Waqiah 
57. Al-Hadid 
58. Al-Mujadilah 
59. Al-Hashr 
60. Al-Mumtahanah 
61. As-Saf 
62. Al-Jumah 
63. Al-Munafiqun 
64. At-Taghabun 
65. At-Talaq 
66. At-Tahrim 
67. Al-Mulk – 
68. Al-Qalam 
69. Al-Haqqah 
70. Al-Maarij 
71. Nuh 
72. Al-Jinn 
73. Al-Muzammil 
74. Al-Mudaththir 
75. Al-Qiyamah 
76. Al-Insan 
77. Al-Mursalat 
78. An-Naba 
79. An-Naziat 
80. ‘Abasa 
81. At-Takwir 
82. Al-Infitar 
83. Al-Mutaffifin 
84. Al-Inshiqaq 
85. Al-Buruj 
86. At-Tariq 
87. Al-Ala 
88. Al-Ghashiyah 
89. Al-Fajr 
90. Al-Balad 
91. Ash-Shams 
92. Al-Layl 
93. Adh-Dhuha 
94. Al-Inshirah 
95. At-Tin 
96. Al-‘Alaq 
97. Al-Qadar 
98. Al-Bayinah 
99. Az-Zalzalah 
100. Al-‘Adiyah 
101. Al-Qariah 
102. At-Takathur 
103. Al-‘Asr 
104. Al-Humazah 
105. Al-Fil 
106. Quraish 
107. Al-Maun 
108. Al-Kauthar 
109. Al-Kafirun 
110. An-Nasr 
111. Al-Masad 
112. Al-Ikhlas 
113. Al-Falaq 
114. An-Nas 
    """)

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