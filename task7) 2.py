def covid(name,temp):
    if temp>98:
        print(name+" is suffering from covid")
    else:
        print(name+" is not suffering from covid")

name = input("enter patient name")
temp=int(input("enter  temp"))
covid(name,temp)




             output
  enter patient name   swetha
  enter temp        99
  swetha is suffering from covid