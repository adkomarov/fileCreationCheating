try:
    count = int(input('enter the number of gigabytes:  '))
except:
    count=1
constGigabyte = 1073741824
size = constGigabyte * count
with open("file.to.create", "wb") as out:
    out.truncate(size)
