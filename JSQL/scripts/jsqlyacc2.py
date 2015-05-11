import os
import codecs
import subprocess
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
    Number num2 = "helo";
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



proc = subprocess.Popen('javac JSQLClass.java',
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        )
stdout_value, stderr_value = proc.communicate('new comm')
#print '\tpass through:', repr(stdout_value)
#print '\tstderr      :', repr(stderr_value)

if 'double' in str(stderr_value):
    print "Incompatible types"
else:
    print 'Compiled successfully'


try:
    proc1 = subprocess.Popen('java JSQLClass',
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        )
#stdout_value, stderr_value = proc.communicate('1')
#print '\tpass through:', repr(stdout_value)
#print '\tstderr      :', repr(stderr_value)
    o = proc1.stdout.read()
    print o
except Exception as err:
    print err




#try:
 #   p = sub.Popen(["javac JSQLClass.java"], stdout=sub.PIPE,shell=True)
  #  out = p.stdout.read()
#except TypeError as err:
 #   print err
#else:
 #   print 'sds'

#try:
 #   p1 = sub.Popen(["java JSQLClass"],stdout=sub.PIPE,shell=True).stdout.read()
  #  print p1
#except IOError as err1:
 #   print err1
#except ArithmeticError as arithmeticError:
 #   print "Error in Arithmetic Calculations"
#except Exception as err2:
 #   s = "Could not run Successfully"
  #  print s

