import socket
import threading

def service(cs, address):
	while True:
		cs.recv(1024)

def main():
	svr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	svr.bind(('', 16720))
	svr.listen(5)
	while True:
		cs, address = svr.accept()
		print 'got connected from', address


if __name__ == '__main__':
	main()