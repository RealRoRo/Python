from array import *
# first = array('i', [12, 23, 34, 4, 5, 6])
# print(first)
# print(first.buffer_info()) #adress and len
# print(len(first))
# print(first.typecode) #type of array
# print(first[0])
#
# copy_first = array(first.typecode, (i for i in first))
# print(copy_first)
# copy_first.reverse()
# print(copy_first)

# n = int(input("Enter limit"))
# arr = array('i', [])
# for i in range(n):
#     arr.append(int(input()))
# print(arr)

# a, b  = input("Enter values to remove").split()
# if int(a) in arr:
#     arr.remove(int(a))
# if int(b) in arr:
#     arr.remove(int(b))
#
# print(arr)

# revArr = array('i', (arr[a] for a in range(len(arr)-1, -1, -1) ))
# print(revArr)


arr2d = array(array , [array('i', [1, 2, 3, 4, 5]), array('i', [1, 2, 3, 4, 5]), array('i', [1, 2, 3, 4, 5])] )
print(arr2d)