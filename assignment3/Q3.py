def count_1 (): 
    list_1= []
    for i in range (10):
        element= int (input ("Enter element: "))
        list_1.append(element)
        print(list_1)
    print ("min:  ",list_1.index(min(list_1)))
count_1()
    
        
    