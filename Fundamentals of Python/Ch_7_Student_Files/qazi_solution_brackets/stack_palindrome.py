__author__ = 'Rafeh'

def stack_palindrome(word):
	if not word:
		return True  # '' == ''[::-1]
	stk = list()
	wordFromStack = ''
	for ch in word:
		stk.append(ch)
	if len(word) == len(stk):
		for ch in range(len(stk)):
			wordFromStack += stk.pop()
	return wordFromStack == word

if __name__ == '__main__':
	word = input("Enter your word here: \n")
	if stack_palindrome(word):
	    print("Palindrome")
	else:
		print("NOT Palindrome")
