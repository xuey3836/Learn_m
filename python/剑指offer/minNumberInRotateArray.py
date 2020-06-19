
def minNumberInRotateArray(rotateArray):
    # write code here
    len_a = len(rotateArray)
    if len_a == 0:
        return 0
    for i in range(len_a-1):
        if rotateArray[i+1] < rotateArray[i]:
            return rotateArray[i+1]

a = [3,4,5,1,2]
minNumberInRotateArray(a)   