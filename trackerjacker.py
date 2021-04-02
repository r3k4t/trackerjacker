import os
import json
import urllib2

print("          +========================================+")
print("          |             TrackerJacker              |")
print("          +========================================+")
print("          |     Author : Rahat Khan Tusar(rkt)     |")
print("          |     Github : https://github.com/r3k4t  |")
print("          +========================================+")

print

while True:

   ip=raw_input("Enter any ip address to track:")
   url="https://ipinfo.io/"
   r=urllib2.urlopen(url + ip)
   d = r.read()
   v =json.loads(d)
    
   print("IP         : "+ v ['ip'])
   print("City       : "+ v ['city'])
   print("Country    : "+ v ['country'])
   print("Region     : "+ v ['region'])
   print("Loc        : "+ v ['loc'])
   print("Org        : "+ v ['org'])
   print("Postal     : "+ v ['postal'])
   print("TimeZone   : "+ v ['timezone'])
   print("Google Map : https://www.google.com/maps/place/"+ v ['loc'])
   print
   raw_input("Press  enter key to stop ........")
   break
