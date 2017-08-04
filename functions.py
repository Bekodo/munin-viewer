import glob

def toFind(service):
    services = { 'cpu': "aws*CPUutilization-day.png",
                'memory': "memory-day.png",
                'eth0': "if_eth0-day.png",
                'netstat': "netstat-day.png",
                'load': "load-day.png",
                'cpu2': "cpu-day.png"
                }
    return services.get(service,"nothing")

def siteDiscard():
    with open('sites.cfg') as file:
        sites = file.read().splitlines()
        return sites

def getChars(service):
    chars = []
    charspath = "/var/www/html/munin/*/*/"
    index = 0
    aux = 0
    chars.append([])
    sdiscard = siteDiscard()
    pattern = toFind(service)
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
