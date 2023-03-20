max_number = 100
min_number = 1

input('Hola! Piensa en un número del {} al {} y lo voy a adivinar. Pulsa [ENTER] para continuar.'
      .format(min_number, max_number))

while True:
    current_number = round((max_number + min_number) / 2)
    if max_number == min_number == current_number:
        print('Deja de trollearme!!')
        break
    answer = input('Tu número es {}? (>/</=)'.format(current_number))
    if answer == '=':
        print('Toma ya!')
        break
    if answer == '<':
        max_number = current_number
    if answer == '>':
        min_number = current_number