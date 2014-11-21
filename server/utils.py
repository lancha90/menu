def is_exist_order(array,order):
	counter=0
	for item in array:
		if item.order == order:
			return counter
		counter+=1
	return -1
