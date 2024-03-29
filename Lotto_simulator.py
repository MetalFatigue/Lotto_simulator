import random

user_selection = []
i = 0
while i < 6:
    while True:

        try:
            number = input("Choose your number")
            number = int(number)
            break
        except ValueError:
            print("It's not a number")
    if number in user_selection:
        print("You can't select the number again")

    elif number >= 1 and number <= 49:
        user_selection.append(number)
        i += 1
    else:
        print("You choose wrong number")

user_selection.sort()
print(user_selection)

draw = []
while len(draw) < 6:
    draw.append(random.randint(1, 49))
    draw.sort()
print(draw)

hit = 0
for element in draw:
   hit += user_selection.count(element)

if hit == 1:
    print(f" You hit {hit} time")
else:
    print(f" You hit {hit} times")
