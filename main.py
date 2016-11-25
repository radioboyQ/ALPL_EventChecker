import configparser


config_location = 'lib/config.ini'

config = configparser.ConfigParser()

config.read(config_location)

print(config['API_KEY']['Client_Secret'])