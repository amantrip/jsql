# dictionary of variable types
symbols = { }


header = ""
functions = ""

<<<<<<< HEAD
     __BODY__

}
'''

s = '''
void main()
{
    Number num1 = 10;
    Number num2 = 11;
    Number num3 = num1 + num2;
    print "Hello world";
    print num1 + num2;
    print (num1 + num2);
}
'''
try:
    body = yacc.parse(s)
    #file_name = os.path.splitext("path_to_file")[0]
    file_name = "JSQLClass.java"
    outfile = codecs.open(file_name, encoding = 'utf-8', mode = 'w')
    outfile.write(javatemplate.replace('__BODY__', body))
    outfile.close()
except Exception as err:
    print err


try:
    p = sub.Popen(["javac JSQLClass.java"], stdout=sub.PIPE,shell=True)
    out = p.stdout.read()
    print out
except Exception as err:
    print err
else:
    print 'Compiled Successfully'

try:
    p1 = sub.Popen(["java JSQLClass"],stdout=sub.PIPE,shell = True)
    out2 = p1.stdout.read()
    print out2
except IOError as err1:
    print err1
except ArithmeticError as arithmeticError:
    print "Error in Arithmetic Calculations"
except Exception as err2:
    s = "Could not run Successfully"
    print s






=======
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
>>>>>>> 404cb27e8b8439f799178bfeaeb8a3855deb5c8e
