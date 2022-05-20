#given 3 integers, return their sums, but if there are duplicate values, don't count those in the sum
#complete the function as your answer
def duplicateSums(a, b, c):
    if a == b and b == c:
        return 0
    res = a + b + c
    if a == b or a == c:
        res -= 2 * a
    if b == c:
        res -= 2 * b
    return res

print(duplicateSums(1,2,3))     #should return 6
print(duplicateSums(2,3,2))     #should return 3
print(duplicateSums(1,1,1))     #should return 0
