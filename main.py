from ossapi import Ossapi, UserLookupKey
import configparser, os, sys

#read from config
config = configparser.ConfigParser()
config.read('config.txt')
client_id = config['oAPI']['client_id']
client_secret = config['oAPI']['client_secret']
if client_id == '' or client_secret == '' :
    sys.exit("Missing API") #sys library

api = Ossapi(client_id, client_secret)
mainMode = 'osu' # osu, mania, taiko, fruits

# print(api.user(13456818).statistics.global_rank) # get global rank
# print(api.user(13456818).statistics.country_rank) # get global rank
# print(api.user(13456818).country_code) # get country code
# print(api.user(13456818).id) # get id
# print(api.user(13456818).username) # get username

#open and import file as lists
list = open("list.txt", "r").readlines()
output = open("output.txt", "w")
print("Processing...")
print(list)

#process
count=len(list)
for X in list:
    X = X.strip('\n') #remove newline character
    try:
        user = api.user(X, mode=mainMode)
        print(user.statistics.global_rank, file=output) # change here for file output
        count = count - 1
        print("Get User", user.username, "|", count , "user left.")
    except Exception as e:
        print("!!! SKIPPED !!!", X)
        print("Error: ", e)
        print("", file=output)

output.close()
print("Done. Check output.txt")
