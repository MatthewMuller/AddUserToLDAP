########################################
# This script will add a user to the ldap
#########################################



# call python program to get info from user
userinput=$(python3 userinputgui.py 2>&1);

#Split the userinput into values in an array
IFS=',' read -ra arr<<< "$userinput"


# ssh into ldap server and add user to the system
sshpass -p ${arr[4]} ssh administrator@141.224.38.247 'echo ${arr[4]} | sudo useradd -p $(openssl passwd -1 ${arr[3]}) ${arr[2]}'
