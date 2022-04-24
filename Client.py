from http import client
import threading
import socket

class Client:
    
    def __init__(self):
    
        self.port = 7976
        self.ip = "localhost"
        self.nick = ''
        self._client_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def run (self):
        try:
            print("> Se conectando em {}".format(self.port))

            self._client_.connect((self.ip, self.port))
            self.nick = input("> Digite o seu nick: ")

            recieve_thread = threading.Thread(target=self.receive)
            write_thread = threading.Thread(target=self.write)

            write_thread.start()
            recieve_thread.start()

        except:
            print("> Conexão fechada")

    def receive(self):
        while True:
            try:
                msg = self._client_.recv(1024).decode('ascii')

                if msg == 'NICKNAME':
                    self._client_.send(self.nick.encode('ascii'))
                
                else:
                    print(msg)
            except:
                print("> Ocorreu algum erro")
                self._client_.close()
                break
    
    def write(self):
        while True:
            msg = "{}:{}".format(self.nick, input('> '))
            self._client_.send(msg.encode('ascii'))