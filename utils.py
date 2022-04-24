import os
from typing import NoReturn


class Console: 

    def __init__(self):
        pass

    def clear (self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def inputInt ( self, txt ) -> int:
        try:
            userInput = input(txt)
            return int(userInput)
        except:
            print("> Por favor digite um numero")
            return self.inputInt(txt)
    
    def choiceAOption ( self, options = [] ):
        try: 
            for index, element in enumerate(options):
                ElementString = "[{}]. {}".format(index, element)
                print(ElementString)
            
            choiceInt = self.inputInt("> Escolha uma opção: ")
            choice = options[choiceInt]
            return choice

        except:
            print("> Por favor escolha uma opção valida")
            return self.choiceAOption

console = Console()