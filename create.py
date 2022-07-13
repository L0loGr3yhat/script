#!/usr/bin/python
#######################
#CIEEE MAU RECODE YA??#
#######################
blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'
yellow='\033[33;1m'

# module

import os,sys,time
from time import sleep

# tampilan
os.system("clear")
sleep(1)
banner ="""\033[34;1m
_          _          ____                _           _
| |    ___ | | ___    / ___|_ __ ___ _   _| |__   __ _| |_                    | |   / _ \| |/ _ \  | |  _| '__/ _ \ | | | '_ \ / _` | __|                   | |__| (_) | | (_) | | |_| | | |  __/ |_| | | | | (_| | |_
|_____\___/|_|\___/   \____|_|  \___|\__, |_| |_|\__,_|\__|                                                        |___/
____         ____          _          _
/ ___|  ___  | __ ) _   _  | |    ___ | | ___                                 \___ \ / __| |  _ \| | | | | |   / _ \| |/ _ \                                 ___) | (__  | |_) | |_| | | |__| (_) | | (_) |
|____/ \___| |____/ \__, | |_____\___/|_|\___/                                                    |___/
  <=========================>
<===[+]Author : Lolo Greyhat===>
<===[+]Script Deface By Lolo===>
  <=========================>"""
sleep(1)
print(banner)
print "\033[34;1mSILAKAN ISI"
title = raw_input("\033[32;1m Title => ")
bgcolor = raw_input("\033[32;1m background color(contoh=black) => ")
copyright = raw_input("\033[32;1m copyright by => ")
image = raw_input("\033[32;1m link gambar (tengah) => ")
heading = raw_input("\033[32;1m Hacked By => ")
message = raw_input("\033[32;1m Pesan. gunakan kode <br> untuk text selanjutnya! => ")
textcolor = raw_input("\033[32;1m Color text(contoh=red) => ")
greet = raw_input("\033[32;1m GREETZ. gunakan kode <br> untuk text selanjutnya! => ")

#Open the index
fo = open("hasil.html","w")

messagescript1 = """<html><head><title>"""

messagescript2 = title

messagescript3 = """</title></head>
<body>
<br>
<body bgcolor="""

messagescript4 = bgcolor

messagescript5 = """><center><br><br></font>
<font face="courier" size="5" color="red">"""


messagescript6 = copyright

messagescript7 = """</font><br><br>
<img src="""

messagescript8 = image

messagescript9 = """ width=450px height=auto></font><br><br><font face="courier new" color="red">"""


messagescript10 = heading


messagescript11 = """</font><br><br><font face="courier new" color="""


messagescript12 = textcolor

messagescript13 =  """ size="5">"""

messagescript14 = message

messagescript15 = """<br><br><font face="courier new" size="5">"""
   
messagescript16 = greet

messagescript17 = """</font>"""

fo.write(messagescript1)
fo.write(messagescript2)
fo.write(messagescript3)
fo.write(messagescript4)
fo.write(messagescript5)
fo.write(messagescript6)
fo.write(messagescript7)
fo.write(messagescript8)
fo.write(messagescript9)
fo.write(messagescript10)
fo.write(messagescript11)
fo.write(messagescript12)
fo.write(messagescript13)
fo.write(messagescript14)
fo.write(messagescript15)
fo.write(messagescript16)
fo.write(messagescript17)

os.system("clear")
os.system("figlet Done!")
print "\033[34;1m ==========================================================="
print "\033[34;1m [+]file script bernama hasil.html"
print "\033[34;1m ==========================================================="
fo.close()
