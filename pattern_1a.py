#quetion1-a
def pattern(n):
    for i in range(0, 5):
        for j in range(0, i+1):
            print("* ",end="")
        print()
pattern(int(input('enter number')))