from ossapi import Ossapi, UserLookupKey

#parse credentials
import configparser
import os
config = configparser.ConfigParser()

#check if config file exist in directory, create a template if not found
if os.path.isfile('config.txt') == 'False' :
    config['API'] = {'client_id': '',
                     'client_secret': ''}
    with open('config.txt', 'w') as configfile:
        config.write(configfile)

#read from config
config.read('config.txt')
client_id = config['API']['client_id']
client_secret = config['API']['client_secret']
api = Ossapi(client_id, client_secret)

#open list
list = open("list.txt", "r")
output = open("output.txt", "w")

#process
print("Processing...")
for X in list:
    X = X.strip('\n') #remove newline character
    user = api.user(X)
    print(user.id, file=output)

output.close()
print("Done. Check output.txt")