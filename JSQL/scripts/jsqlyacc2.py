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

s = '''
void main(String args[])
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
except Exception as err:
    print err
else:
    print 'Compiled Successfully'

try:
    p1 = sub.Popen(["java JSQLClass"],stdout=sub.PIPE,shell=True).stdout.read()
    print 'jejejej'
    print p1
except IOError as err1:
    print err1
except ArithmeticError as arithmeticError:
    print "Error in Arithmetic Calculations"
except Exception as err2:
    s = "Could not run Successfully"
    print s

