#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, socket, sys

cfg = {
	'sockfile' : 'darkadmin.sock',
}

SO_PASSCRED = 16

def main():
	sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, SO_PASSCRED, 1)
	sock.connect(cfg['sockfile'])
	sock.send(' '.join(sys.argv))
	data = sock.recv(1024)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "\033[1G\033[K\033[1;37mExiting... (\033[0mCtrl+C\033[1;37m)"