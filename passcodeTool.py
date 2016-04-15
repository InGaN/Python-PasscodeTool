import sys

def rsa(integer):
	return integer
	
with open(sys.argv[1], 'r') as my_file:
	str = ''
	for line in my_file:
		input = (line.rstrip()).split('|')
		for x in range(0, len(input)):
			for y in range(0, len(input[x])):
				str += '{:x}'.format(rsa(ord(input[x][y])))			
			str += '|'
			
	print(str)