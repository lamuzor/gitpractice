import module
my_list = [i+1 for i in range(20)]

print(module.suml(my_list) )
print(module.prodl(my_list))

print('*'*15)


zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))

