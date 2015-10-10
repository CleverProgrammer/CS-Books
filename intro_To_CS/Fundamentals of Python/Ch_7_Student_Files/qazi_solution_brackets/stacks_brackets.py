def bracketsBalance(thing):
	stk = list()
	for ch in thing:
		if ch in ['(', '[']:
			stk.append(ch)
		elif ch in [')', ']']:
			if len(stk) == 0:
				return False
			chFromStack = stk.pop()
			if ch == ')' and chFromStack != '(' or \
	         ch == ']' and chFromStack != '[' :
				return False
	if len(stk) == 0:
		return True

if __name__ == '__main__':
	   thing = input("Enter your expression here: \n")
	   if bracketsBalance(thing):
		   print("OK")
	   else:
		   print("NOT OKAY")