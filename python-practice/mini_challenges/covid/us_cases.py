import urllib.request

fp = urllib.request.urlopen("https://www.worldometers.info/coronavirus/country/us/")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)