__author__ = 'Rafeh'


def main():
    filename = input("Enter a file name: \n")
    infile = open(filename, mode='r')
    outfile = open("mydata.out", mode='w')
    for line in infile:
        print(line, file=outfile)
    infile.close()

if __name__ == '__main__':
   main()