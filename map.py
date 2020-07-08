# # number of elements
# n = int(input("Enter number of elements : "))
#
# # Below line read inputs from user using map() function
# a = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
#
# print("\nList is - ", a)

a = [1,56,23,1,23,34,345,435,345,564]

print("even filter(): ",list(filter(lambda n: n%2 == 0, a)))
print("Map() double: ",list(map(lambda n:n*2, a)))

from functools import reduce

print("reduce() sum: ", reduce(lambda x, y: x+y , a))
