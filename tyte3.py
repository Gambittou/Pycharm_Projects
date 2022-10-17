import urllib.request, urllib.parse, urllib.error
"""This is the simplest version of a web browser that I could find written
in python, in just 3 lines of code (not including the import information) you 
can read all the data from yahoo's UK web page. This shows the power of Python"""
fhand = urllib.request.urlopen('http://uk.yahoo.com/')
for line in fhand:
    print(line.decode().strip())