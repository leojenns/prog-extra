#welcome


#maak een programma dat op basis van de input van een kleur de gebruiker verteld wat te doen bij een stoplicht.

#vraag1
kleur = input("wat is de kleur van het verkeerslicht?")


if kleur == 'groen':
    print("Gassen!!!!!!!!!!!!!")
elif kleur == 'geel':
    print("stoppen als het kan!!")
elif kleur == 'rood':
    print('stoppen!!')
else:
    print("wtf dit is geen stoplicht geen mushrooms meer!!!!")




#vraag 2 


#input vragen en al vast alles letters klein maken.
s = input('wat is de string:')
s = s.lower()

#een string maken die de reverse is van s.
reversed_string = reversed(s)

#controleren of de string het zelfde is.
if s == reversed_string:
    print('palingdroom')
else:
    print('geen palingdroom')



#vraag 3

def is_schrikkeljaar(jaar):
    if jaar % 4 == 0 and jaar % 100 != 0:
        schrikkeljaar = True
    elif jaar % 400 == 0:
        schrikkeljaar = True
    else:
        schrikkeljaar = False
    return schrikkeljaar



# vraag 4
def suggestie():
    weer = input('Wat is het weer vandaag:')
    if weer == 'zonnig':
        print('Het is een zonnige dag, trek je schoenen aan.')
    elif weer == 'Regenachtig':
        print('Oops! Het is een regenachtig, trek je laarzen aan.')
    else:
        print('dit weer bericht ken ik niet.')
suggestie()


#vraag 5

# vraag de gebruiker om 2 getallen:

getal1 = float(input())
getal2 = float(input())

# vraag de gebruiker om de bewerking.

bewerking  = input('wat is de bewerking:')2


# voer de bewerking uit en print de som.
if bewerking == "+":
    resultaat = getal1 + getal2
    print(f'{getal1} + {getal2} = {resultaat}')
elif bewerking == "-":
    resultaat = getal1 - getal2
    print(f'{getal1} - {getal2} = {resultaat}')
elif bewerking == "*":
    resultaat = getal1 * getal2
    print(f'{getal1} * {getal2} = {resultaat}')
elif bewerking == "/":
    resultaat = getal1 / getal2
    print(f'{getal1} / {getal2} = {resultaat}')
else:
    print('ken de bewerking niet')


#vraag 6

s = input("wat is de tekst:")

s = s[::-1] # of reversed(s)

print(s)

# met forloop:

for char in s:
    print(char, end="")



#vraag 7

for getal in range(1,51):
    if getal % 3 == 0 and getal % 5 ==0:
        print("fizzbuzz")
    elif getal % 3 == 0:
        print('fizz')
    elif getal % 5 ==0:
        print("buzz")
    else:
        print(getal)















