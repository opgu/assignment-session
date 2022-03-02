#dictionary


d = {"easy": "hard","slow": "fast"}
d.clear()
print('d =',d)


d = {"easy": "hard","slow": "fast"}
x =d.copy()
print('x: ',x)


keys = {"easy": "hard","slow": "fast"}
x = d.fromkeys(keys)
print(x)


marks = {'maths':45,'english':78}
print(marks.get('maths'))



marks = {'maths':45,'english':78}
print(marks.items())


sales ={'apple': 5,'banana': 4}
element = sales.pop('apple')
print('popped element is: ', element)



d = {"easy": "hard","slow": "fast"}
d1 = {'slow': "fastly"}
d.update(d1)
print(d)


sales ={'apple': 5,'banana': 4}
print(sales.values())


people ={"name": "utkarsh","age": "20"}
name = people.setdefault('name')
print('name =',name)






