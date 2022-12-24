#AWS Service Inventory

#Create a list of services using Python. IE: S3, Lambda, EC2, etc

#1. The list should be empty initially.
#2. Populate the list using append or insert.
#3. Print the list and the length of the list.
#4. Remove two specific services from the list by name or by index.
#5. Print the new list and the new length of the list.


my_list = []
len(my_list)

my_list.append('S3')

my_list.append('lambda')

my_list.append('compute')

my_list.append('database')

my_list.append('security')

my_list.append('cloudfront')

my_list.append('sns')

my_list.append('vpc')

my_list.append('auto-scaling')
print(my_list)

size = len(my_list)
print(size)

del my_list[5]
del my_list[7]

print(my_list)
