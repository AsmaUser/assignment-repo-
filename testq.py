u =[]
die= [1,2,3,4,5,6]

def main():
    user_try= int (input("Enter a number of try: "))
    for x in range (user_try):
        func1(u)
    func2(u, die)

def func1(u):
    num_die= input ("Enter a numbers: ")
    numbers = num_die.split()
    for n in numbers:
        if n:
            u.append(int(n))
        else:
            break
     
    
def func2 (u,die):
    for i in die:
        print(i, " : ", u.count(i))
        
main()
        
    