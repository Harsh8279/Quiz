import socket 
import pickle
host = socket.gethostname()

port=1000

s = socket.socket()

s.connect((host,port))


give_usr_name = input(s.recv(1024).decode())
s.send(give_usr_name.encode())
give_password = input(s.recv(1024).decode())
s.send(give_password.encode())

w_d = s.recv(1024)
try:
	msg = w_d.decode()
	print(msg,type(msg))
except:
	menus = pickle.loads(w_d)
	#print(menus)
	while True:
		for i in menus:
			print(i)
				
		ch = input("Enter your choice : ")
		
		s.send(ch.encode())
		
		
		
		w_d_ques = s.recv(1024)
			
		try:
			msg_reply = w_d_ques.decode()
			if (msg_reply)=='Exit':
				s.close()
				break
			else:
				print(msg_reply)
		except:
			ques = pickle.loads(w_d_ques)
			ans=[]
			#print(ques[-1])
			
			for i in range(ques[-1]):
				for j in ques[i]:
					print(j)
				ans.append(input('Answer :'))
				print()
			#print(ans)
			
			s.send(pickle.dumps(ans))
			
		