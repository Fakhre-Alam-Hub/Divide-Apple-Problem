def func():
    try:
        n = int(input("Enter the number of Apple : "))

        mn = int(input("Enter the minimum number : "))

        mx = int(input("Enter the maximum number : "))

    except Exception as e:
        print("Your input is invalid...")
        func()



    for x in range(mn,mx):
        if n%x == 0:
            print(f" {x} is a divisor of {n} ")
        else:
            print(f" {x} is not a divisor of {n} ")


func()