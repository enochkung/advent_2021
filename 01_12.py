from utils import bin_to_decimal


def day_1():
	increase_count = 0
	for index, i in enumerate(input):
		if index == 0:
			continue
		if input[index - 1] < i:
			increase_count += 1
	
	return increase_count


def day_1b():
	with open('day_1b_input.txt') as f:
		lines = f.readlines()
	input = []
	for line in lines:
		input.append(int(line.split('\n')[0]))
	
	increase_count = 0
	for index, i in filter(lambda _index: _index[0] + 4 <= len(input), enumerate(input)):
		if sum(input[index:index + 3]) < sum(input[index + 1: index + 4]):
			increase_count += 1
	return increase_count


def day_2():
	with open('day_2_input.txt') as f:
		lines = f.read().splitlines()
	input = []
	for line in lines:
		input.append((line.split()[0], line.split()[1]))
	
	init = [0, 0]
	for direction, intervals in input:
		if direction == 'forward':
			init[0] += int(intervals)
		elif direction == 'up':
			init[1] -= int(intervals)
		elif direction == 'down':
			init[1] += int(intervals)
	
	return init[0] * init[1]


def day_2b():
	with open('day_2b_input.txt') as f:
		lines = f.read().splitlines()
	input = []
	for line in lines:
		input.append((line.split()[0], line.split()[1]))
	
	init = [0, 0, 0]
	for direction, intervals in input:
		if direction == 'forward':
			init[0] += int(intervals)
			init[1] += init[2] * int(intervals)
		elif direction == 'up':
			init[2] -= int(intervals)
		elif direction == 'down':
			init[2] += int(intervals)
	
	return init[1] * init[0]


def day_3():
	with open('day_3_input.txt') as f:
		input = f.read().splitlines()
	
	N = len(input[0])
	gamma_rate = ''
	epsilon_rate = ''
	for i in range(N):
		entries = [X[i] for X in input]
		len_0 = sum(x == '0' for x in entries)
		len_1 = sum(x == '1' for x in entries)
		gamma_rate += '0' if len_0 > len_1 else '1'
		epsilon_rate += '1' if len_0 > len_1 else '0'
	
	return bin_to_decimal(gamma_rate) * bin_to_decimal(epsilon_rate)


def day_3b():
	with open('day_3b_input.txt') as f:
		input = f.read().splitlines()
	
	o_input = input.copy()
	c_input = input.copy()
	N = len(input[0])
	
	for i in range(N):
		o_entries = [X[i] for X in o_input]
		c_entries = [X[i] for X in c_input]
		o_len_0 = sum(x == '0' for x in o_entries)
		o_len_1 = sum(x == '1' for x in o_entries)
		c_len_0 = sum(x == '0' for x in c_entries)
		c_len_1 = sum(x == '1' for x in c_entries)
		if o_len_0 > o_len_1:
			o_input = [x for x in o_input if x[i] == '0'] if len(o_input) > 1 else o_input
		else:
			o_input = [x for x in o_input if x[i] == '1'] if len(o_input) > 1 else o_input

		if c_len_0 > c_len_1:
			c_input = [x for x in c_input if x[i] == '1'] if len(c_input) > 1 else c_input
		else:
			c_input = [x for x in c_input if x[i] == '0'] if len(c_input) > 1 else c_input

		if len(o_input) == 1 and len(c_input) == 1:
			break
	return bin_to_decimal(o_input[0]) * bin_to_decimal(c_input[0])


if __name__ == '__main__':
	print(day_3b())
