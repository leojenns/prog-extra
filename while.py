

#while true
lst = []

while True:
    invoer = input()
    if invoer == 'stop':
        break
    else:
        invoer = float(invoer)
        lst.append(invoer)


print(f'de optelling van de getallen  = {sum(lst)}')



#while conditie

invoer = input()
total = 0
while invoer != 'stop':
    invoer = float(invoer)
    total = total + invoer
    invoer = input()

print(f'de optelling van de getallen  = {total}')
