import sys

print ("Napište číslem kolik je nyní hodin (1 až 24): ")
print ("Pozor! Pište jenom celá čísla! Nikoli písmena a desetinná čísla.")
čas = int(input())

print ("\nNapište svoje jméno: ")
jméno = input()

if(čas < 12 and čas >= 1):
	čas = "ráno"

elif(čas >= 12 and čas < 18):
	čas = "odpoledne"

elif(čas >= 18 and čas < 25):
	čas = "večer"

else:
	sys.exit("Stala se chyba! " + jméno + " , zkontroluj, zda jsi zadal správně číslo!")

print ("\nDobrý " + str(čas) + ", ti přeji, " + jméno + " :-)")






