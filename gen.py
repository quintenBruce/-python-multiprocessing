import random

dict = { '.' : 1, 'O' : 2}



grid = []

for i in range(1000):
    k = []
    for j in range(1000):
        k.append(random.choice(list(dict.items()))[0])
    
    grid.append(k)



with open("test2.in", "w") as txt_file:
    for line in grid:
        txt_file.write("".join(line) + "\n") 





############################################################################################

# import argparse
# parser = argparse.ArgumentParser()

# parser.add_argument('-i', action="store", dest="inputFile")
# parser.add_argument('-o', action="store", dest="outputFile")
# parser.add_argument('-p', action="store", dest="PROCESSES", type=int, default=1)

# args = parser.parse_args()
# print(args.inputFile, args.outputFile, args.PROCESSES)

############################################################################################


# bee = [5, 6, 7]
# arr = [[4]]
# arr.append([bee[0], bee[1], bee[2]])

# print(arr)






############################



# arr = [5, 6, 7]
# print(arr[1:2])


# l = 6
# t = 4

# k = l//t
# p = l%t

# print(k, p)
# print("\n")

# c = 1
# i = 0
# for i in range(k, l-p, k):
#     print(c, ": ",i-k, i)
#     c += 1





