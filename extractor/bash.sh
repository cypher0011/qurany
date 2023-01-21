#give the shakihs name
curl -s https://mp3quran.net/eng | grep -A1 '<a rel="alternate" ' | grep -v -E "(http|https)://[a-zA-Z0-9./?=_%:-]*" | sed 's/--//g' | tr -s " " > shakihs_name.txt


#the links of shaiks
curl -s https://mp3quran.net/eng | grep -A1 '<a rel="alternate" ' | grep  -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*" > shaiks_links.txt

#make the link to dirc 
for i in $(cat shaiks_links.txt | cut -d '/' -f5) ; do echo \"w\":\"$i\" ;done > dirc_shaiks.txt
