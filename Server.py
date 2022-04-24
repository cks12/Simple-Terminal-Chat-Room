import socket, threading
from typing import NoReturn

class Server:
    def __init__ (self):
        self.port = 7976
        self.host = "localhost"
        self._clients_ = []
        self._nickname_ = []
        self._server_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def _broadcast_ (self, msg) -> NoReturn:
        for client in self._clients_:
            client.send(msg)
    
    def _handle_(self,client) -> NoReturn:
        while True:
            try:
                msg = client.recv(1024)
                self._broadcast_(msg)
            except:
                index = self._clients_.index(client)
                self._clients_.remove(client)
                client.close()
                nick = self._nickname_[index]
                self._nickname_.remove(nick)
                self._broadcast_('{} Saiu da sala'.format(nick))
                break
    
    def receive (self) -> NoReturn:
        while True:
            client, addres = self._server_.accept()
            print("> O {} se conectou".format(addres))
            client.send("NICKNAME".encode('ascii'))
            nick = client.recv(1024).decode('ascii')
            
            self._nickname_.append(nick)
            self._clients_.append(client)
            self._broadcast_("{} Entrou no server". format(nick).encode("ascii"))
            print("> {} setou como nick {}".format(addres, nick))

            thread = threading.Thread(target=self._handle_, args=(client,))
            thread.start()
    
    def run(self) -> NoReturn:
        print("> Tentando rodar o servidor")
        try:
            self._server_.bind((self.host, self.port))
            print("> Server rodando na porta:{}".format(self.port))
            self._server_.listen()
            self.receive()
        except:
            print("> Servidor fechado!")

