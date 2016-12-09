import poplib
host = "202.141.80.10"
port = 995
email = username
pwd = password

server = poplib.POP3_SSL(host, port)
try: 
	server.user(email)
	if('+OK'):
		server.pass_(pwd)
		if("+OK Logged in."):
			print "Bhai, login chal gaya"
		else:
			print "Bhai, pass galat hai"
except poplib.error_proto:
	print "Bhai, kuch problem hai"
