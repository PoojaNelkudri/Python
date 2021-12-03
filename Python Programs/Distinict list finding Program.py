def distinict(list1):
 
    # initialize a null list
    distinict_list = []
     
 
    for x in list1:
      
        if x not in distinict_list:
            distinict_list.append(x)
    
    for x in distinict_list:
        print (x)
     
   
list1 = [10, 10, 20, 30, 40,50, 60,50]
print("the unique values from 1st list is")
distinict(list1)
 
 
list2 =[1, 2, 3, 3, 1, 5, 3, 3, 5]
print("\nthe unique values from 2nd list is")
distinict(list2)
