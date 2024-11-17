# join two lists, using '+' operator
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
newlist = list1 + list2
print(newlist)

# join lists using append
for i in list2:
    list1.append(i)
    print(list1)

# adding list4 at the end of list3
list3 = [1, 2, 3, 4, 5]
list4 = [6, 7, 8, 9, 10]
list3.extend(list4)
print(list3)
