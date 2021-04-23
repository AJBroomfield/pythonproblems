option = ['rock','paper','scissors']

first = str(input("Player 1. rock, paper or scissors? ")).lower()
second = str(input("Player 2. Rock, Paper or Scissors? ")).lower()


a = option.index(first)
b = option.index(second)

results=[['Draw', 'P2 Win', 'P1 Win'],['P1 Win', 'Draw','P2 Win'],['P2 Win','P1 Win','Draw']]

print(results[a][b])

