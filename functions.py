import glob
import configparser
from collections import OrderedDict

def getConf():
    services = OrderedDict()
    config = configparser.RawConfigParser()
    config.read('services.ini')
    for key in config.items('services'):
        services[key[0]]=key[1]
    return services

def siteDiscard():
    with open('sites.cfg') as file:
        sites = file.read().splitlines()
        return sites

def getChars(services,service):
    chars = []
    charspath = "/var/www/html/munin/*/*/"
    index = 0
    aux = 0
    chars.append([])
    sdiscard = siteDiscard()
    pattern = services.get(service,"nothing")
    for char in glob.iglob(charspath + pattern):
        d = char.split('/')
        values = {'site': d[5], 'service': d[6], 'char': d[7] }
        if not d[6] in sdiscard:
            chars[index].append(values)
            aux += 1
            if (aux % 4) == 0:
                index += 1
                chars.append([])
    return chars
