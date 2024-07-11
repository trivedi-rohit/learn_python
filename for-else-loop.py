# for-else loop
'''numb = (2, 3 , -1, 5, 6, 7, 0, 53, 78, 48, 55)
list1 = []
for i in numb:
    list1.append(i)
    if i == 0:
        print ("Number Found")
        # break
        pass
else:        #! else part will only be executed when for loop run successfully without any error or break/pass
    print("The list of numbers is: ",list1)'''


numb = (2, 3 , -1, 5, 6, 7, 0, 53, 78, 48, 55)
for i in numb:
    print (i)
    if i == 0:
        break
else:        
    print("The list executed succesfully.")
print("Done")