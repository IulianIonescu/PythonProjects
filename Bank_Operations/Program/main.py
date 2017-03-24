from functions import *

print('Meniu (0) Testare Automata(1)')
alegere = int(input())
if alegere == 0:
    functie_test_user()
else:
    functie_test_automata()