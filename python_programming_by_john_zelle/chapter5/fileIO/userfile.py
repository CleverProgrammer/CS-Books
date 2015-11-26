__author__ = 'Rafeh'

def main():

	infilename = input("Enter the file name from where the data should be read from: \n")
	outfilename = input("Enter the file name to where the data should be written to: \n")
	infile = open(infilename, mode='r')
	outfile = open(outfilename, mode='w')
	for line in infile:
		first, last = line.split()
		uname = (first + " " + last).lower()
		print(uname, end = '\n', file=outfile)
	infile.close()
	outfile.close()
	print("Usernames from {0} have been written to {1}".format(infilename,outfilename))

if __name__ == '__main__':
	main()

