

def binary_search(list,item):

	low = 0
	high = len(list)-1
	idx = -1
	while low <= high:
		mid = (low+high)//2
		if item == list[mid]:
			idx = mid
			break
		if item < list[mid]:
			high = mid-1
		else:
			low = mid+1
			
	return idx


if __name__ == "__main__":

	my_list = [1,3,5,7,9]
	print(binary_search(my_list,7))
	print(binary_search(my_list,10))