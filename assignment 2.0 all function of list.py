# list function

mylist = ["c","c++","python"]
mylist.append("html")
print(mylist)


mylist = ["c","c++","python"]
mylist.clear()
print(mylist)

mylist =["c","c++","python"]
newlist = mylist.copy()
print("copied list:",newlist) 


mylist = ["c","c++","python"]
mylist1 =["html","css"]
mylist.extend(mylist1)
print('mylist:', mylist)


mylist = ["c","c++","python"]
index =mylist.index('python')
print ('the index of python: ',index)


mylist = ["c","c++","python"]
mylist.insert(1,'java')
print(mylist)


mylist = ["c","c++","python"]
return_value = mylist.pop(2)
print('return value:', return_value)


mylist = ["c","c++","python"]
mylist.remove('c++')
print(mylist)


mylist = ["c","c++","python"]
mylist.sort()
print(mylist)

