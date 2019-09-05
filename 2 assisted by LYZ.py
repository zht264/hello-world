list=[]
while True:
        numbers=input("enter a number:")
        if numbers=="done":
                print (sum(list),len(list),max(list),min(list))
                break
        try:
                numbers=float(numbers)
                list.append(numbers)
        except:
                print ("please enter a number")
                

            



