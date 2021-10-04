import socket
import time
HOST = '134.209.103.10' 
PORT = 5000 
listacc=[]
while True:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Start listening...')
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = (conn.recv(1024).decode())
            print(data)
            message=data.split(':')
            if message[0]=='Add acc':
               listacc.append(message[1])
               print("Account :",len(listacc))
               print(message[1])
               print(listacc)
               conn.sendall("OK".encode())
               break
            if message[0]=='Reg acc':
               if len(listacc)>0:
                  sendacc=listacc[0]
                  print(sendacc)
                  conn.sendall(sendacc.encode())
                  del listacc[0]
                  s.close()
                  break
               else:
                  sendacc="No acc"
                  conn.sendall(sendacc.encode()) 
                  print(sendacc)
                  break                  
            if not data:
                break         
            
