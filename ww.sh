if ! which mplayer > /dev/null; then
   echo -e "Command not found! Install? (y/n) \c"
   read answer
   if [ "$answer" = "y" ]
   then
      sudo apt-get install mplayer
   fi
fi
