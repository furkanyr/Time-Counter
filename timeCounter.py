import time

def time_counter(num):
    counter = num
    while counter > 0:
        print(counter)
        time.sleep(1)
        counter -= 1
    print("time is over!")

num = input("Enter the second: ")

while num.isdigit() == False:
    num = input("Enter the second: ")

num = int(num)
time_counter(num)