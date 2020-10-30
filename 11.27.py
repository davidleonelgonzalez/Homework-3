# David Gonzalez
# 1630338

dictionary = {}
integer = 1
c = 1

for integer in range(1, 6):
    jn = int(input("Enter player {}\'s jersey number:\n" .format(integer)))
    r = int(input("Enter player {}\'s rating:\n" .format(integer)))
    print()
    if jn < 0 and jn > 99 and r < 0 and r > 9:
        print("invalid entry")
        break
    else:
        dictionary[jn] = r
        
print("ROSTER")
for jn, r in sorted(dictionary.items()):
    print("Jersey number: %d, Rating: %d" % (jn, r))

choice = ''

while choice.upper() != 'Q':
    print("\nMENU\n"
          "a - Add player\n"
          "d - Remove player\n"
          "u - Update player rating\n"
          "r - Output players above a rating\n"
          "o - Output roster\n"
          "q - Quit\n")

    choice = input("Choose an option:\n")

    if choice == "a":
        jn = int(input("Enter a new player\'s jersey number:\n" .format(integer)))
        r = int(input("Enter the player\'s rating:\n" .format(integer)))
        dictionary[jn] = r

    elif choice == "d":
        jn = int(input("Enter a jersey number:\n"))
        if jn in dictionary.keys():
            del dictionary[jn]

    elif choice == "u":
        jn = int(input("Enter a jersey number:\n"))
        if jn in dictionary.keys():
            r = int(input("Enter a new rating for player:\n"))
            dictionary[jn] = r

    elif choice == "r":
        rate = int(input("Enter a rating:\n"))
        print("ABOVE {}" .format(rate))
        for jn, r in sorted(dictionary.items()):
            if r > rate:
                print("Jersey number: %d, Rating: %d" % (jn, r))

    elif choice == "o":
        print("ROSTER")
        for jn, r in sorted(dictionary.items()):
            print("Jersey number: %d, Rating: %d" % (jn, r))




