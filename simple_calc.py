# add function
def add(*nums):
	sum = 0
	for x in nums:
		sum += x
	return sum

print(add(4, 5))

# multiplication function
def multiply(*numbers):  
    product = 1
    for x in numbers:
        product *= x  
    return product 

print(multiply(1, 2))
