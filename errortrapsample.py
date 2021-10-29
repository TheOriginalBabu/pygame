import random



bmFtZXZhcmlhYmxl = input("Hello, what is your name? ")

YWdldmFy = False

def YWdlZnVuY3Rp():
    try:
        YWdldmFy = int(input("What is your age? "))
        return YWdldmFy
    except:
        print("ur done")
        YWdlZnVuY3Rp()

YWdldmFy = YWdlZnVuY3Rp()

aW5zdWx0 = ["Dinky","Doofus","Stupid","Dumbbutt","Disgrace to society"]

if YWdldmFy < 10:
    aW5zdWx0 = aW5zdWx0[random.randrange(0,2)]
elif YWdldmFy >= 10 and YWdldmFy == 16:
    aW5zdWx0 = aW5zdWx0[random.randrange(0,3)]
elif YWdldmFy >= 16:
    aW5zdWx0 = aW5zdWx0[random.randrange(3,4)]

if YWdldmFy < 0:
    print("Negative age number.")

print(f"{bmFtZXZhcmlhYmxl}, you are a {aW5zdWx0}")