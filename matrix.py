matrix1 = []
matrix2 = []

counter = 0
counter1 = 0
bol = True

while True:
    userInput = input(
        "matrix1:")
    matrix1.append(userInput.split())
    if counter > 0:
        if len(matrix1[counter - 1]) != len(matrix1[counter]):
            if ["*"] in matrix1:
                matrix1.pop()
                break
            else:
                print("error!")
                bol = False
                break
    elif "*" in matrix1:
        break
    counter += 1

# to int the indexes :
print("-------- matrix 1 ---------")
for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        matrix1[i][j] = int(matrix1[i][j])
        print(matrix1[i][j], end=" ")
    print()
    n = len(matrix1)
    m = len(matrix1[i])


while bol:
    userInput2 = input(
        "matrix 2:")
    matrix2.append(userInput2.split())
    if len(matrix2[counter1 - 1]) != len(matrix2[counter1]):

        if ["="] in matrix2:
            matrix2.pop()

            if len(matrix1[0]) != len(matrix2):
                print("error !")
                break
            print("-------- matrix 2 ---------")
            for i in range(len(matrix2)):

                for j in range(len(matrix2[i])):
                    matrix2[i][j] = int(matrix2[i][j])
                    print(matrix2[i][j], end=" ")
                print()
                l = len(matrix2)
                k = len(matrix2[i])

            if m == l:
                result = [[0 for j in range(k)]for i in range(n)]
                for i in range(n):
                    for j in range(k):
                        for z in range(m):
                            result[i][j] += matrix1[i][z]*matrix2[z][j]

                for i in range(n):
                    for j in range(k):
                        print(result[i][j], end=" ")
                    print()

                break
        else:
            print("error !")
            break
    counter1 += 1


for i in range(len(matrix2)):
    for j in range(len(matrix2[i])):
        matrix2[i][j] = int(matrix2[i][j])
