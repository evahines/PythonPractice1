#given a list of integers, swap the first and last elements, return the new list with swapped elements
#complete the function as your answer
def swap(numList):
    newList = numList
    temp = newList[0]
    newList[0] = newList[-1]
    newList[-1] = temp
    return newList

print(swap([1,2,3,4,5]))        #should print [5,2,3,4,1]
print(swap([5,2,3,4,1]))        #should print [1,2,3,4,5]
print(swap([7,4,7,2,3,6,3]))    #should print [3,4,7,2,3,6,7]
