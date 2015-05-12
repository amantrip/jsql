import glob
import codecs
import subprocess
from jsqlyacc import yacc


fileN = raw_input('Please Enter the jsql file name you want to compile: ')
file = fileN+'.jsql'
filebuffer = open(file,'r')
x = filebuffer.read()

javatemplate = '''
import java.util.*;
import org.json.simple.parser.*;


public class '''+fileN+''' {

     __BODY__

}
'''

try:
    body = yacc.parse(x)
    file_name = fileN+".java"
    outfile = codecs.open(file_name, encoding = 'utf-8', mode = 'w')
    outfile.write(javatemplate.replace('__BODY__', body))
    outfile.close()
except Exception as err:
    print err
    exit()

print file_name

proc = subprocess.Popen('javac '+file_name,
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        )
stdout_value, stderr_value = proc.communicate('new comm')



if 'double' in str(stderr_value) or 'error' in str(stderr_value):
    print str(stderr_value)
else:
    print 'Compiled successfully'


try:
    proc1 = subprocess.Popen('java -cp ~/Documents/PLT/jsql/JSQL/org/json/simple/parser '+fileN,
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

