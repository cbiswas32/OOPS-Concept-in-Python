list1=[3,6,7,8,4,75,23,123,67]


# for item in list1:
#     if item%2==0:
#         list2.append(item)

list2=[item for item in list1 if item%2==0]
print(list2)        