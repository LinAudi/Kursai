print("Puzzle Pieces. \n")

def corresponding(integers1,integers2):
    if len(integers1) != len(integers2):
        return False
    sum_result = integers1[0]+integers2[0]

    for number in range(len(integers1)):
        if integers1[number] + integers2[number] != sum_result:
           return False
    else:
        return True


print(corresponding([1,2,3,4],[4, 3, 2, 1]))
print(corresponding([1,8,5,0,-1,7],[0,-7,-4,1,2,-6]))
print(corresponding([1,2],[-1,-1]))
print(corresponding([9,8,7],[7,8,9,10]))


