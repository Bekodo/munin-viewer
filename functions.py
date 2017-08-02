import glob

def getChars():
    chars = []
    index = 0
    aux = 0
    chars.append([])
    for char in glob.iglob("/var/www/html/munin/*/*/aws*CPUutilization-day.png"):
        d = char.split('/')
        values = {'site': d[5], 'service': d[6], 'char': d[7] }
        chars[index].append(values)
        aux += 1
        if (aux % 4) == 0:
            index += 1
            chars.append([])
    return chars
