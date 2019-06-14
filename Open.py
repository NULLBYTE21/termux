# -*- coding: utf-8 -*-
import os
import sys
import time
from time import sleep

P = "\x1b[35m"
C = "\x1b[36m"
GR = "\x1b[37m"
def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0/90)

os.system("clear")
Termux=(gt+"""
 ####### ##### #####   ##    ## #    # #   #   
    #    #     #    #  # #  # # #    #  # #
    #    ##### #####   #  ##  # #    #  ##
    #    #     #    #  #      # #    # #  #
    #    ##### #     # #      #  #### #    #
 ===============================================
""")
slowprints(semut)
print(gt+"")
input('\nPress enter to continue...')
sleep(2)
slowprints("[!] Making Termux Properties directory...")
sleep(4)
try:
      os.mkdir("/data/data/com.termux/files/home/.termux")
except:
      pass
slowprints("[!] Success Making Termux Properties directory!")
sleep(3)
slowprints("[!] Making Setup file...")
sleep(1)

shortcutkey = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LE                       >
script = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
script.write(shortcutkey)
script.close()
sleep(1)
slowprints("[!] Success Making Setup file...")
sleep(2)
slowprints("\n[!] Setting up setup file...")
sleep(2)
os.system("termux-reload-settings")
slowprints("[!] Successfully !! Making Termux Shortcut Key, Terimakasih sudah memakai script                        >
os.system("rm -f key.py")
os.system('exit') 
