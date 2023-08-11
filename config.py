#parse config
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