
f = open("change.html", "r")
r = open("result.txt", "w")
# read each line
for line in f:
    char1 = 0
    char2 = 0
    # read until the end of the line
    while ( char1 + 24 <= len(line) ):
        
        print(char1 + 24)
        print(len(line))
        # find the end of each group of colored characters
        for c in range(char1 + 24, len(line), 1):
            print("index: " + str(c))
            if line[c] == ">":
                char2 = c
                print("char2 is now " + str(c))
                break
        
        # splice the group of colored characters
        code = line[char1 : char2 + 1]
        print("code: " + str(code))

        # write converted html to bbcode to the file
        r.write("[color=#" + str(line[char1 + 16 : char1 + 22]) + "]" + str(line[char1 + 23 : char2 - 3]) + "[/color]")

        # set the startpoint of the next group of characters
        char1 = char2 + 1
        print(char1, char2)
    r.write("\n")
    





