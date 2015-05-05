# dictionary of variable types
symbols = { }


header = ""
functions = ""

def p_start(t):
	'start : statement'
	global body
	body = t[1]
    
def p_statement_conc(t):
	'statement : statement statement'
	t[0] = "%s\n %s"%(t[1],t[2])

def p_statement_value(t):
	'statement : value'
	print "asddd"
	t[0] = "%s;"%t[1]