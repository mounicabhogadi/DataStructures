# HelloWorld with while loop

x = 6
temp = 1
while temp <= x:
    print(f"{temp}.  Hello World")
    temp += 1

# reverse

x = 1
temp = 6
while temp >= x:
    print(f"{temp}.  Hello World")
    temp -= 1

# Take integer as an input and counts down from that number to zero, printing even numbers

x = 10
while x >= 0:
    if x % 2 == 0:
        print(f"{x} is even")

    else:
        print(f"{x} is odd")
    x -= 1
