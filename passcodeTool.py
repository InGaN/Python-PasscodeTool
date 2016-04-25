import sys	

def validateKeys(p, q):	
	if(p==q):
		print("You may not enter 2 identical numbers")
		return False
	if not (isPrime(p)):		
		if not (isPrime(q)):
			print("p and q are not prime numbers")
		else:
			print("p is not a prime number")
		return False
	if not (isPrime(q)):
		print("q is not a prime number")
		return False	
	return True

def isInteger(s):
	try: 
		int(s)
		return True
	except ValueError:
		return False	
	
def isPrime(n):
	if(isInteger(n) == False):
		print(n + " is not a number")
		return False
	if int(n) > 1:
		for i in range(2,int(n)):
			if(int(n)%i)==0:
				return False
		return True
	else: 
		return False

def areCoPrime(p, q):
	for n in range(2, min(p, q) + 1):
		if p%n == q%n == 0:
			#print(str(p) + "," + str(q) + " are not coprime")
			return False
	#print(str(p) + "," + str(q) + " are coprime")
	return True
		
def generateKeys(p, q): 
	n = int(p)*int(q)
	phi = (int(p)-1)*(int(q)-1)
	
	for e in range(3, phi, 2):
		if areCoPrime(e, phi):
			break
	for d in range(3, phi, 2):
		if (d*e)%phi == 1:
			break	
		
	return [[e, n],[d, n]]
		
	
def rsa(integer, exponent, modulo):	
	x = pow(int(integer), int(exponent), int(modulo))
	return x

def encrypt(e, n):
	with open(sys.argv[2], 'r') as my_file:
		for line in my_file:
			print(line)
	with open(sys.argv[2], 'r') as my_file:
		output = ''
		for line in my_file:
			input = (line.rstrip()).split('|')
			for x in range(0, len(input)):
				for y in range(0, len(input[x])):
					output += str(rsa(ord(input[x][y]), e,n))
					if y != len(input[x])-1:
						output += ","
					#output += '{:02x}'.format(rsa(ord(input[x][y]), e,n))
				output += '|'
		output = output[:-1] # remove trailing pipe
		print(output)
	f = open('output.txt', 'w')
	f.write(output)

def decrypt(d, n):
	with open(sys.argv[2], 'r') as my_file:
		output = ''
		for line in my_file:
			input = (line.rstrip()).split('|')
			for x in range(0, len(input)):
				val = input[x].split(',')

				for y in range(0, len(val)):
					g = str(val[y])
					output += str(chr(rsa(int(g),d,n)))
					#if y != len(val)-1:
						#output += ","
				if x%3 == 2:
					output += '\n'
				else:
					output += '|'
		print(output)
	
def main():
	requestInput()	
	
def requestInput():
	if(sys.argv[1] == "-d"):
		print("decrypt")
		d = input("Please input KV pair as d,n: ").split(',')				
		if(len(d) != 2) or (isInteger(d[0]) == False) or (isInteger(d[1]) == False):
			print("invalid Key Value pair")			
		else:
			decrypt(d[0],d[1])
	elif(sys.argv[1] == "-e"):
		print("encrypt")
		validate = False
		while (validate == False):
			p = input("Please enter a prime for p: ")		
			q = input("Please enter a prime for q: ")
			validate = validateKeys(p,q)
		x = generateKeys(p,q)
		print("Public:("+str(x[0][0])+","+str(x[0][1])+") Private:("+str(x[1][0])+","+str(x[1][1])+")")
		character = 'c'
		myVal = ord(character)
		y = pow(myVal,x[0][0],x[0][1])
		print(character + " = " + str(myVal) + " > " + str(y) + " > " + str(pow(y,x[1][0],x[1][1])) + " > " + chr(pow(y,x[1][0],x[1][1])))		
		encrypt(x[0][0],x[0][1])
	elif(sys.argv[1] == "-h"):
		print("-d file | decrypt file")
		print("-e file | encrypt file")
		print("-h | help")
	else:
		print("unknown command, please type 'python passcodeTool.py -h' for help")
		
if __name__ == "__main__":
    main()