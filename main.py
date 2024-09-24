my_bool = True
my_bool2 = False

x = 4

if my_bool:
    print("Villkoret är sant")

i = 1

while i <= 10:
    print(i)
    i += 1

game_over = False

while not game_over:
    print("Spel spel spel spel spel")
    print("Spel spel spel spel spel")
    print("Spel spel spel")
    print("Spel spel spel spel spel spel spel")
    answer = input("Vill du spel? ")
    if answer != "spel":
        game_over = True

print("Inte spel")