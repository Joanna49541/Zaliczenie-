import random

class Symbol:
    suits = ['papier','nożyce','kamień']
    def __init__(self, suit):
        self.suit = suit
    def __repr__(self):
        return self.suits[self.suit]
class Tab:
    def __init__(self):
        self.symbols = []
        for i in range(3):
            self.symbols.append(Symbol(i))
        random.shuffle(self.symbols)
    def show_symbol(self):
        return self.symbols[random.randint(0,2)]  

class Player:
    def __init__(self, name):
        #self.wins = 0 
        self.symbol = None
        self.name = name
symbol1 = Symbol(0)
symbol2 = Symbol(1)   
symbol3 = Symbol(2) 


print("Takie masz możliwości: ") 
print(symbol1, symbol2, symbol3)

print("Taka jest zawartość: ")
tab = Tab()
for symbol in tab.symbols:
    print(symbol)  

class Game:
    def __init__(self):
        name1 = input("Gracz 1 - Podaj imię: ")
        name2 = input("Gracz 2 - Podaj imię: ")
        self.tab = Tab()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def draw(self, p1name, p1symbol, p2name, p2symbol):
        d = "{} wyciagnął {}, {} wyciągnął {}"
        d = d.format(p1name, p1symbol, p2name, p2symbol)  
        print(d)

    def wins(self, winner):
        w = "Tę rundę wygrywa: {}"
        w = w.format(winner)
        print(w)

    def play_game(self):
        symbols = self.tab.symbols
        print("Zaczynamy rozgrywkę!")
        scorep1 = 0
        scorep2 = 0
        while len(symbols) >= 2:
            m = "Naciśnij q, aby wyjść " 
            response = input(m)
            if response == 'q':
                break    
            p1symbol = self.tab.show_symbol()
            p2symbol = self.tab.show_symbol()
            p1name = self.p1.name
            p2name = self.p2.name
            self.draw(p1name, p1symbol, p2name, p2symbol)
     
            if p1symbol.suit == 0 and p2symbol.suit == 1 or p1symbol.suit == 1 and p2symbol.suit == 2 or p1symbol.suit == 2 and p2symbol.suit == 0:
                scorep2 += 1
                # self.p1.wins += 1
                #self.wins(self.p2.name)
               
            elif p1symbol.suit == 0 and p2symbol.siut == 2 or p1symbol.suit == 1 and p2symbol.suit == 0 or p1symbol.suit == 0 and p2symbol.suit == 2:
                scorep1 += 1
                #self.p1.wins += 1
                #self.wins(self.p1.name)
                 
            elif p1symbol.suit == p2symbol.suit:
                scorep1 += 1
                scorep2 += 1
                #self.p1.wins += 1
                #self.wins(self.p1.name)
                #self.p2.wins += 1
                #self.wins(self.p2.name)

        print(p1name, "ma", scorep1, "a", p2name, "ma", scorep2)

        #win = self.winner(self.p1, self.p2)
        #print("Wojna skończona - wygrał {}".format(win))

    #def winner(self, p1, p2):
        #if p1.wins > p2.wins:
       #     return p1.name
       # if p1.wins < p2.wins:
       #     return p2.name
       # return "jest remis!"    

game = Game()
game.play_game()                  

