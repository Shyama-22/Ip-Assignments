def squaring(x):
  n = x*x
  return n
def generateData():
  N = int(input("number of input-output pairs : "))
  f = open("IOpair.txt", "w")
  f.write(str(N))
  f.close()
  for i in range(N):
    p = int(input())
    result = squaring(p)
    # Storing input in a file
    f = open("File"+str(i)+".txt", "w")
    f.write(str(p))
    f.close()
    # Storing output in a file
    f1 = open("ResultFile"+str(i)+".txt", "w")
    f1.write(str(result))
    f1.close()

generateData()