def bin_to_decimal(bin_string):
	N = len(bin_string)
	return sum([2**(N-1-i) * int(bin_string[i]) for i in range(N)])
