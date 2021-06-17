#to remove intersection of 2 nd set from the 1 st set


s1={10,25,40,50,60}
s2={10,20,30,35 ,50,55}
s1.difference_update(s2)
print(s1)
print(s2)



      Output
      
{40, 25, 60}
{35, 10, 50, 20, 55, 30}

[Program finished]