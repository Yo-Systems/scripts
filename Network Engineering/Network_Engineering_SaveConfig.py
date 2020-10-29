#!/usr/bin/env python

import getpass
import sys
import telnetlib

user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

f = open('filewithswitchIPs')

for line in f:
	print("Getting running config from Switch " + line)
	HOST = line
	tn = telnetlib.Telnet(HOST)

	tn.read_until("Username: ")
	tn.write(user + "\n")
	if password:
		tn.read_until("Password: ")
		tn.write(password + "\n")

	tn.write("terminal length 0\n")
	tn.write("show run\n")
	tn.write("exit\n")

	reoutput = tn.read_all()
	saveoutput = open("switch" + HOST, "w")
	saveoutput.write(readoutput)
	saveoutput.close
	print tn.read_all()



