import mysql.connector as mc

import socket 

import pickle

import collections

host = socket.gethostname()

port = 1000

s = socket.socket()

s.bind((host,port))

s.listen(1)

a,c = s.accept()

usr_name=""
password=''

con = mc.connect(host="localhost",user="root",password="",database="project_networking_db")


cur  = con.cursor()


ask_usr_name = "Enter your user name :"
a.send(ask_usr_name.encode())
usr_name = a.recv(1024).decode()

ask_password = "Enter your password :"
a.send(ask_password.encode())
password = a.recv(1024).decode()

flag =0

q = "select * from student where username='"+usr_name+"' and password='"+password+"'"

#print(q)

cur.execute(q)

cur.fetchall()

total_ques=0
#print(cur.rowcount)

if cur.rowcount>0:
	flag = 1
	menus=[
		'1. Rules and Regulations',
		'2. Give Exam',
		'3. Show Result',
		'4. Exit'
	]
	a.send(pickle.dumps(menus))
	while True:
		ch =int(a.recv(1024).decode())
		
		if ch==1:
			rules = "\n\t1.Attempt All the questions. \n\t2.There 4 options select anyone of them.\n\t3.Do not press any key for Interruption.\n"
			a.send(rules.encode())
		elif ch==2:
			
			q = "select question,op1,op2,op3,op4 from quiz"
			
			cur.execute(q)
			
			ques = cur.fetchall()
			
			#print(ques,type(ques))
			
			
			
			que_lst=[]
			
			for i in ques:
				que_lst.append(list(i))
				#print(i)
			
			que_lst.append(len(ques))
			total_ques=len(ques)
				
			#print(que_lst,type(que_lst))
			
			a.send(pickle.dumps(que_lst))
			
			client_ans = pickle.loads(a.recv(1024))
			
			q = "select answer from quiz"
			
			cur.execute(q)
			
			
			
			#print(client_ans)
			ans=[]
			
			for i in cur.fetchall():
				for j in i:
					#print(j)
					ans.append(j)
					
			#print("Db Answer : ",ans)
			#print("Client Answer :",client_ans)
			
			cnt=0
			
			for i in range(len(ans)):
				if (ans[i]!=client_ans[i]):
					cnt+=1
			total = len(ques)
			res = total-cnt
			#print("Result is ",res)
			
			q = "update student set result="+str(res)+" where username='"+usr_name+"'"
			
			#print(q)
			
			cur.execute(q)
			
			
			
		elif ch==3:
			#a.send("Result".encode())
			
			q = "select result from student where username='"+usr_name+"'"
			
			cur.execute(q)
			
			for i in cur.fetchall():
				for j in i:
					result= str(j)
			
			
			q = "select * from quiz"
			
			cur.execute(q)
			cur.fetchall()
			tot_ques=str(cur.rowcount)
			r_msg = "\n\t"+result+' out of '+tot_ques+"\n"
			a.send(r_msg.encode())
					
			
		elif ch ==4:
			a.send("Exit".encode())
			a.close()
			break
			
		else:
			a.send("Wrong Input :(".encode())
		
		
		
else:
	flag = 0
	a.send("Hey !! contact to admin plz you are not authorized".encode())

	
	



