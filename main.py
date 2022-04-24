from secrets import choice
from Server import Server
from Client import Client
from utils import console

def main():
    ops = ["Server", "Client"]
    console.clear()
    choice = console.choiceAOption(options=ops)

    server = Server()
    client = Client()

    if choice == "Server":
        server.run()
    
    if choice == "Client":
        client.run() 

if __name__ == "__main__":
    main()