#!/usr/bin/python3 
import time, os, math
timezone=time.timezone
zonename=time.tzname
print("TimeZone: ", timezone)
print("ZomeName: ", zonename)
hrs=int(time.strftime("%H"))
mnt=int(time.strftime("%M"))
sec=int(time.strftime("%S"))
dom=int(time.strftime("%d"))
dow=int(time.strftime("%w"))
now=int(time.strftime("%U"))
mon=int(time.strftime("%m"))
doy=int(time.strftime("%j"))
noy=int(time.strftime("%Y"))
dim=hrs * 60 + mnt
dis=dim * 60 + sec
rev=dis / 240
print("hrs:", hrs)
print("min:", mnt)
print("sec:", sec)
print("dom:", dom)
print("dow:", dow)
print("now:", now)
print("mon:", mon)
print("doy:", doy)
print("noy:", noy)
print("dim:", dim)
print("dis:", dis)
print("did:", rev)