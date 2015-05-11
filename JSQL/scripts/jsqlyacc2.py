import glob
import codecs
import subprocess
from jsqlyacc import yacc

javatemplate = '''
import java.util.*;


public class JSQLClass {

     __BODY__

}
'''

for filename in glob.glob1('.','*.jsql'):
    file = filename

filebuffer = open(file,'r')
x = filebuffer.read()

try:
    body = yacc.parse(x)
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

