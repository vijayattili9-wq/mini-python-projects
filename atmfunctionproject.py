# ATM project
balance = 0
def credit():
    global balance
    try:
        amount = int(input("enter the amount: "))
        if amount <=0:
            print("enter positive amount")
        else:    
            balance += amount
            print(f"${amount} successfully credited to your account...")
    except:
        print(f"enter the numerics.....")
def debit():
    global balance
    amount = float(input("enter the amount: "))
    if amount <=0:
        print(f"please enter positive amount: ")
    elif amount> balance:
        print(f"insufficient balance")    
    else:
        balance -= amount
        print(f"successfully debited your account")

def check_balance():
    global balance
    print(f"current balance:${balance}")

def menu():
    while True:
        print("1.credit")
        print("2.debit")
        print("3.check_balance")
        print("4.exit")
        choice = int(input("enter the choice: "))
        if choice == 1:
            credit()

        elif choice == 2:
             debit()
        elif choice == 3:
             check_balance()
        elif choice ==4:
            print(f"thank you for using ATM") 
            break
        else:
            print(f"invalid choice....please try again...")                

menu() 