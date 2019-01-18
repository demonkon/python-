#! /usr/bin/env python
#coding=utf-8
import bluetooth 
import os
import time
from bluetooth import *

while True:	
	device = discover_devices(lookup_names=True)
	for i in device:
		if i[1] == "什么鬼":
			os.popen('shutdown -l ')
	time.sleep(10)
	

#os.popen('shutdown -l ')
