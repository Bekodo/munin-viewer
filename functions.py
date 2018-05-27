import glob
import configparser
from collections import OrderedDict

def getConf(type):
    if (type == 'services'):
        section = 'services'
    else :
        section = 'discard_servers'
    elements = OrderedDict()
    config = configparser.RawConfigParser(allow_no_value=True)
    config.read('services.ini')
    for key in config.items(section):
        elements[key[0]]=key[1]
    return elements

def getChars(services,service):
    chars = []
    charspath = "/var/www/html/munin/*/*/"
    index = 0
    aux = 0
    sdiscard = getConf('servers')
    pattern = services.get(service,"nothing")
    for char in glob.iglob(charspath + pattern):
        d = char.split('/')
        values = {'site': d[5], 'service': d[6], 'char': d[7] }
        if not d[6] in sdiscard:
            chars.append(values)
    return chars
