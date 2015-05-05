
import sys
sys.path.insert(0,"../..")

if sys.version_info[0] >= 3:
    raw_input = input

# Build the lexer
import ply.lex as lex

# Reserved words
reserved = (
    'BREAK', 'CASE', 'CONTINUE', 'DEFAULT', 'NUMBER',
    'ELSE', 'FOR', 'IF', 'STRING', 'RETURN', 'SWITCH', 'TYPEDEF',
    'WHILE', 'TRUE', 'FALSE', 'NULL', 'VOID' , 'BOOLEAN', 'LIST', 'JSON', 'PRINT'
    )

tokens = reserved + (

    # Literals (identifier, Number constant, string constant)
    'ID', 'NCONST', 'SCONST',
    
    # Operators (+,-,*,/,%,|,&,~,^, ||, &&, !, <, <=, >, >=, ==, !=, ~~, ^^)
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'OR', 'AND', 'NOT', 'XOR', 
    'LOR', 'LAND', 'LNOT',
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',
    'UNION', 'INTERSECTION',
    
    # Assignment (=, *=, /=, %=, +=, -=, &=, ^=, |=)
    'EQUALS', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL', 'PLUSEQUAL', 'MINUSEQUAL',
    'ANDEQUAL', 'XOREQUAL', 'OREQUAL',

    # Increment/decrement (++,--)
    'PLUSPLUS', 'MINUSMINUS',

    # Conditional operator (?)
    'CONDOP',
    
    # Delimeters ( ) [ ] { } , . ; :
    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE',
    'COMMA', 'PERIOD', 'SEMI', 'COLON',

    # Ellipsis (...)
    'ELLIPSIS',
    )

# Completely ignored characters
t_ignore           = ' \t\x0c'

# Operators
t_PLUS             = r'\+'
t_MINUS            = r'-'
t_TIMES            = r'\*'
t_DIVIDE           = r'/'
t_MOD              = r'%'
t_OR               = r'\|'
t_AND              = r'&'
t_NOT              = r'~'
t_XOR              = r'\^'
t_LOR              = r'\|\|'
t_LAND             = r'&&'
t_LNOT             = r'!'
t_LT               = r'<'
t_GT               = r'>'
t_LE               = r'<='
t_GE               = r'>='
t_EQ               = r'=='
t_NE               = r'!='
t_UNION            = r'<>'
t_INTERSECTION     = r'><'

# Assignment operators

t_EQUALS           = r'='
t_TIMESEQUAL       = r'\*='
t_DIVEQUAL         = r'/='
t_MODEQUAL         = r'%='
t_PLUSEQUAL        = r'\+='
t_MINUSEQUAL       = r'-='
t_ANDEQUAL         = r'&='
t_OREQUAL          = r'\|='
t_XOREQUAL         = r'^='

# Increment/decrement
t_PLUSPLUS         = r'\+\+'
t_MINUSMINUS       = r'--'

# ?
t_CONDOP           = r'\?'

# Delimeters
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_LBRACKET         = r'\['
t_RBRACKET         = r'\]'
t_LBRACE           = r'\{'
t_RBRACE           = r'\}'
t_COMMA            = r','
t_PERIOD           = r'\.'
t_SEMI             = r';'
t_COLON            = r':'
t_ELLIPSIS         = r'\.\.\.'

# Identifiers and reserved words

reserved_map = { }
for r in reserved:
    if( r == 'NUMBER' or r == 'STRING' or r == 'LIST' or r == 'BOOLEAN' or r == 'JSON'):
        reserved_map[r.lower().capitalize()] = r;
    else:
        reserved_map[r.lower()] = r
    
def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value,"ID")
    return t

# Number literal
t_NCONST = r'((\d+)([\.\d+])(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])? | \d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# String literal
t_SCONST = r'\"([^\\\n]|(\\.))*?\"'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Comments
def t_comment(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    
# Preprocessor directive (ignored)
def t_preprocessor(t):
    r'\#(.)*?\n'
    t.lexer.lineno += 1
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()

# Test it out
data = '''
main() {
    print "Hello world";
    Number num1 = 10;
    Number num2 = 11;
    print num1 + num2;
    Json js1 = { "First Name" : "Abhyuday", "Last Name" : "Polineni" };
    Jso2 js2 = { "First Name" : "Akhilesh", "Last Name" : "Mantripragada" };
    print js1 + js2;
}
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    #print tok