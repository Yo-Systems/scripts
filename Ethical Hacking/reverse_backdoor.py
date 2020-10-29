#!/usr/bin/env python

import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("10.10.10.3", 4444))