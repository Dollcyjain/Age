def detect(b):
    b = str(b)
    if len(b) >= 4:
        return True
    return False


def age100(b, pa):
    if detect(b):
        return b + 100
    return pa + (100 - b)


def age_in_2090(b, pa):
    if detect(b):
        return 2090 - b
    return 2090 - (pa - b)


def choice():
    while True:
        user_inp = input("Enter 'q' to quit or Enter 's' to show your age in 2090: ")
        if user_inp == 's':
            age = age_in_2090(age_or_year, present_year)
            print(f"Your age in 2090 will be {age}")
            break
        elif user_inp == 'q':
            break
        else:
            print("Not a valid input!!\nPlease try again.")


def func():
    age = age100(age_or_year, present_year)
    print(f"You will turn 100 in the year {age}")
    choice()


def program():
    if a == 1:
        if detect(age_or_year):
            if present_year - age_or_year > 150:
                print("It seems that you are the oldest person.")
                exit()
            elif age_or_year > present_year:
                print("You are not yet born.")
                exit()
            else:
                func()
        else:
            if age_or_year > 150:
                print("It seems that you are the oldest person.")
                exit()
            else:
                func()
    elif a == 2:
        if detect(age_or_year):
            if age_or_year > present_year:
                print("You are not yet born.")
                exit()
            else:
                print(f"Your current age is {present_year - age_or_year}")
        else:
            if age_or_year > 150:
                print("It seems that you are the oldest person.")
                exit()
            else:
                print(f"Your current age is {age_or_year}")
    else:
        print("Not a valid option.\nPlease try again.")


if __name__ == '__main__':
    age_or_year = int(input("Enter your Age or Year of your birth: "))
    present_year = int(input("Enter the present year: "))
    print("What you want to know:\n\t1. Future Data\n\t2. Current Data")
    a = int(input())
    program()
    while True:
        c = input("Enter 'q' to quit and 'c' to continue: ")
        if c == 'c':
            age_or_year = int(input("Enter your Age or Year of your birth: "))
            present_year = int(input("Enter the present year: "))
            print("What you want to know:\n\t1. Future Data\n\t2. Current Data")
            a = int(input())
            program()
        else:
            exit()
