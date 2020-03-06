list1=["abhi","sahil","saksham"]
list2=["software engineer","civil engineer","doctor"]
zipped1=list(zip(list1,list2))
print(zipped1)
zipped2=dict(zip(list1,list2))
print(zipped2,end='\n\n')
zipped3=zip(list1,list2)
for (a,b) in zipped3:
    print(a,b)


