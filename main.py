from ossapi import Ossapi, UserLookupKey
import configparser, os, sys

config = configparser.ConfigParser()
#read from config
config.read('config.txt')
client_id = config['API']['client_id']
client_secret = config['API']['client_secret']
if client_id == '' :
    sys.exit("Missin API") #sys library

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