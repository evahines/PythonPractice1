#have this function return True or False, do two given numbers add up to 10?
#complete the function as your answer
def addup10(a, b):
    return (a + b) == 10

x = int(input("First num: "))
y = int(input("Second num: "))
print(addup10(x, y))
