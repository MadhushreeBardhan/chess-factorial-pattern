
#quetion1-b Assignment-1

def pattern(n):
      for i in range(0, n):
           for j in range(0, i + 1):
                print("* ", end=" ")
           print("\r")
      for i in range(n, 0 , -1):
          for j in range(0, i):
               print("* ", end=" ")
          print("\r")

pattern(int(input("enter number")))