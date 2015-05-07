import os
import codecs
import subprocess as sub
from jsqlyacc import yacc

javatemplate = '''
import java.util.*;

public class JSQLClass {

     __BODY__
}
'''

'''
Number main() {
    
    print "Hello world";
    Number num1 = 10;
    Number num2 = 11;
    print num1 + num2;
    print (num1 + num2);
    Json js1 = "{ 'First Name' : 'Abhyuday', 'Last Name' : 'Polineni' }";
    Json js2 = "{ 'First Name' : 'Akhilesh', 'Last Name' : 'Mantripragada' }";
    Json js3 = (js1 + js2);
}
'''

s = '''
void main() {
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
    p1 = sub.Popen(["java JSQLClass"],stdout=sub.PIPE)
    out2 = p1.stdout.read()
    print out2
except IOError as err1:
    print err1
except ArithmeticError as arithmeticError:
    print "Error in Arithmetic Calculations"
except Exception as err2:
    s = "Could not run Successfully"
    print s






