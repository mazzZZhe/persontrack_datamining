def parsefile(name):
	"""
		input file every line like:p2 (c2,s1,200,320) (c3,s1,420,500)
		output list :[['c2', 's1', 200, 320], ['c3', 's1', 420, 500]]
	"""
	file = open(name)
	print('file state',file.closed)
	alllines = file.readlines()
	l = []
	for eachline in alllines:
		eachlinelist = eachline.split()
		eachlinelist_ = [parsetracevector(x) for x in eachlinelist if x[0]!='p']
		eachlinelist_.insert(0,eachlinelist[0])
		l.append(eachlinelist_)
		print('current line:'+str(eachlinelist))
	file.close()
	return(l)


def parsetracevector(string):
	"""
		input string :'(c1,s1,200,320)'
	"""
	string = string.strip('(')
	string = string.strip(')')
	string = string.split(',')
	string[2] = int(string[2])
	string[3] = int(string[3])
	return string


	
if __name__ == '__main__':
	parsefile('swdata.txt')
