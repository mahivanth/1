phone={}
def add():
    name=input("Enter the name:").lower()
    n=int(input("enter the phn no:"))
    phone[name]={n}

def sort():
    s=sorted(phone)
    for name in s:
        print(name,":",phone[name])

def search():
    name=input("enter the name to search:").lower()
    if name in phone:
        n = phone[name]
        print(n)

while True:
    print("\n Options")
    print("1.ADD")
    print("2.Sort and Display")
    print("3.Search")
    print("4.End")

    c=input("enter the option (1-4):")

    if c == "1":
        add()

    elif c == "2":
        sort()

    elif c == "3":
        search()

    elif c == "4":
        break

    else:
        print("Enter the valid option")
          
          
