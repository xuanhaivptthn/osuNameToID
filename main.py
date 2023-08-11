from ossapi import Ossapi, UserLookupKey
from config import client_id, client_secret
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