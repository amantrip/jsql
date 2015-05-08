import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from jsqllex import tokens

# translation-unit:

def p_translation_unit_1(t):
    'translation_unit : external_declaration'
    print "p_translation_unit_1"
    t[0] = t[1]
    print t[0]
    pass

def p_translation_unit_2(t):
    'translation_unit : translation_unit external_declaration'
    print "p_translation_unit_2"
    t[0] = t[1] + t[2]
    print t[0]
    pass

# external-declaration:

def p_external_declaration_1(t):
    'external_declaration : function_definition'
    print "p_external_declaration_1"
    print t[1]
    t[0] = t[1]
    pass

def p_external_declaration_2(t):
    'external_declaration : declaration'
    print "p_external_declaration_1"
    pass
    
# function-definition:

def p_function_definition_1(t):
    'function_definition : declaration_specifiers declarator declaration_list compound_statement'
    print "p_function_definition_1"
    pass

def p_function_definition_2(t):
    'function_definition : declarator declaration_list compound_statement'
    print "p_function_definition_2"
    pass

def p_function_definition_3(t):
    'function_definition : declarator compound_statement'
    print "p_function_definition_3"
    pass

def p_function_definition_4(t):
    'function_definition : declaration_specifiers declarator compound_statement'
    print "p_function_definition_4"
    t[0] = "public static " + t[1] + t[2] + t[3]
    print t[0]
    pass
    
# declaration:
'''
def p_declaration_1(t):
    'declaration : JSON ID SEMI'
    t[0] = "JSONObject " + t[2] + " = " + "wapper()" + t[3] + "\n"
    print "p_declaration_1"
    print t[0]
    pass
    
    
def p_declaration_2(t):
    'declaration : JSON ID EQUALS SCONST SEMI'
    print "p_declaration_2"
    t[0] = "JSONObject " + t[2] + " = " + " wapper(" + t[4] + ");\n"
    print t[0]
    pass
  
def p_declaration_3(t):
    'declaration : JSON ID EQUALS ID SEMI'
    print "p_declaration_3"
    t[0] = "JSONObject " + t[2] + " = " + t[4] + ";\n"
    print t[0]
    pass
 
def p_declaration_6(t):
    'declaration : JSON init_declarator_list SEMI'
    print "p_declaration_6"
    if t[1].strip() == "JSONObject":
        print "hel"
    elif t[1].strip() == "String" or t[1].strip() == 'double' or t[1].strip() == "List" or t[1].strip() == "boolean":
        t[2] = t[2].replace("_TYPE_", t[1].strip())
    t[0] = t[1] + t[2] + t[3] + "\n"
    print t[0]
    pass
'''   

def p_declaration_4(t):
    'declaration : declaration_specifiers init_declarator_list SEMI'
    print "p_declaration_4"
    if t[1].strip() == "JSONObject":
        print "hel"
    elif t[1].strip() == "String" or t[1].strip() == 'double' or t[1].strip() == "List" or t[1].strip() == "boolean":
        t[2] = t[2].replace("_TYPE_", t[1].strip())
    t[0] = t[1] + t[2] + t[3] + "\n"
    print t[0]
    pass

def p_declaration_5(t):
    'declaration : declaration_specifiers SEMI'
    print "p_declaration_5"
    t[0] = t[1] + t[2] + "\n"
    print t[0]
    pass

# declaration-list:

def p_declaration_list_1(t):
    'declaration_list : declaration'
    print "p_declaration_list_1"
    t[0] = t[1]
    print t[0]
    pass

def p_declaration_list_2(t):
    'declaration_list : declaration_list declaration '
    print "p_declaration_list_2"
    t[0] = t[1] + t[2]
    print t[0]
    pass
    
# declaration-specifiers
def p_declaration_specifiers_1(t):
    'declaration_specifiers : type_specifier declaration_specifiers'
    print "p_declaration_specifiers_1"
    t[0] = t[1] + t[2]
    print t[0]
    pass
    
def p_declaration_specifiers_2(t):
    'declaration_specifiers : type_specifier'
    print "p_declaration_specifiers_2"
    print t[1]
    t[0] = t[1]
    pass
    
# type-specifier:
def p_type_specifier(t):
    '''type_specifier : NULL
                      | STRING
                      | NUMBER
                      | LIST
                      | BOOLEAN
                      | JSON
                      | VOID
                      '''
    print "p_type_specifier"
    if(t[1] == 'Number'):
        t[1] = "double"
    elif t[1] == 'Json':
        t[1] = "JSONObject"
    t[0] = t[1] + " "
    print t[0]
    pass
    
# init-declarator-list:

def p_init_declarator_list_1(t):
    'init_declarator_list : init_declarator'
    print "p_init_declarator_list_1"
    t[0] = t[1]
    print t[0]
    pass

def p_init_declarator_list_2(t):
    'init_declarator_list : init_declarator_list COMMA init_declarator'
    print "p_init_declarator_list_2"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

# init-declarator

def p_init_declarator_1(t):
    'init_declarator : declarator'
    print "p_init_declarator_1"
    t[0] = t[1]
    print t[0]
    pass

def p_init_declarator_2(t):
    'init_declarator : declarator EQUALS initializer'
    print "p_init_declarator_2"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

def p_declarator_1(t):
    'declarator : direct_declarator'
    print "p_declarator_1"
    t[0] = t[1]
    print t[0]
    pass

# direct-declarator:

def p_direct_declarator_1(t):
    'direct_declarator : ID'
    print "p_direct_declarator_1"
    t[0] = t[1]
    print t[0]
    pass

def p_direct_declarator_2(t):
    'direct_declarator : LPAREN declarator RPAREN'
    print "p_direct_declarator_2"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

def p_direct_declarator_3(t):
    'direct_declarator : direct_declarator LBRACKET constant_expression_opt RBRACKET'
    print "p_direct_declarator_3"
    if t[3] is None:
        t[0] = t[1] + t[2] + t[4]
    else:
        t[0] = t[1] + "[] = new _TYPE_ [" + t[3] + "]" 
    print t[0]
    pass

def p_direct_declarator_4(t):
    'direct_declarator : direct_declarator LPAREN parameter_type_list RPAREN '
    print "p_direct_declarator_4"
    t[0] = t[1] + t[2] + t[3] + t[4]
    print t[0]
    pass

def p_direct_declarator_5(t):
    'direct_declarator : direct_declarator LPAREN identifier_list RPAREN '
    print "p_direct_declarator_5"
    t[0] = t[1] + t[2] + t[3] + t[4]
    print t[0]
    pass

def p_direct_declarator_6(t):
    'direct_declarator : direct_declarator LPAREN RPAREN '
    print "p_direct_declarator_6"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

def p_constant_expression_opt_1(t):
    'constant_expression_opt : empty'
    print "p_constant_expression_opt_1"
    print t[0]
    pass

def p_constant_expression_opt_2(t):
    'constant_expression_opt : constant_expression'
    print "p_constant_expression_opt_2"
    t[0] = t[1]
    print t[0]
    pass
    
# parameter-type-list:

def p_parameter_type_list_1(t):
    'parameter_type_list : parameter_list'
    print "p_parameter_type_list_1"
    t[0] = t[1]
    print t[0]
    pass

def p_parameter_type_list_2(t):
    'parameter_type_list : parameter_list COMMA ELLIPSIS'
    print "p_parameter_type_list_2"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

# parameter-list:

def p_parameter_list_1(t):
    'parameter_list : parameter_declaration'
    print "p_parameter_list_1"
    t[0] = t[1]
    print t[0]
    pass

def p_parameter_list_2(t):
    'parameter_list : parameter_list COMMA parameter_declaration'
    print "p_parameter_list_2"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

# parameter-declaration:
def p_parameter_declaration_1(t):
    'parameter_declaration : declaration_specifiers declarator'
    print "p_parameter_declaration_1"
    t[0] = t[1] + t[2]
    print t[0]
    pass

def p_parameter_declaration_2(t):
    'parameter_declaration : declaration_specifiers'
    print "p_parameter_declaration_2"
    t[0] = t[1]
    print t[0]
    pass

# identifier-list:
def p_identifier_list_1(t):
    'identifier_list : ID'
    print "p_identifier_list_1"
    t[0] = t[1]
    print t[0]
    pass

def p_identifier_list_2(t):
    'identifier_list : identifier_list COMMA ID'
    print "p_identifier_list_2"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass
    
# initializer:

def p_initializer_1(t):
    'initializer : assignment_expression'
    print "p_initializer_1"
    t[0] = t[1]
    print t[0]
    pass

def p_initializer_2(t):
    '''initializer : LBRACE initializer_list RBRACE
                   | LBRACE initializer_list COMMA RBRACE'''
    print "p_initializer_2"
    if len(t) == 4:
        t[0] = t[1] + t[2] + t[3]
    else:
        t[0] = t[1] + t[2] + t[3] + t[4]
    print t[0]
    pass

# initializer-list:

def p_initializer_list_1(t):
    'initializer_list : initializer'
    print "p_initializer_list_1"
    t[0] = t[1]
    print t[0]
    pass

def p_initializer_list_2(t):
    'initializer_list : initializer_list COMMA initializer'
    print "p_initializer_list_2"
    print t[1]
    print t[2]
    print t[3]
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass
    
# statement:

def p_statement(t):
    '''
    statement : labeled_statement
              | expression_statement
              | compound_statement
              | selection_statement
              | iteration_statement
              | jump_statement
              | print_statement
              '''
    print "p_statement"
    t[0] = t[1]
    print t[0]
    pass
    
# print-statement:
def p_print_statement_1(t):
    'print_statement : PRINT expression_opt SEMI'
    print "p_print_statement_1"
    t[0] = "System.out.println(" + t[2] + ")" + t[3] + '\n'
    print t[0]
    pass
    
# labeled-statement:
def p_labeled_statement_1(t):
    'labeled_statement : CASE constant_expression COLON statement'
    print "p_labeled_statement_1"
    t[0] = t[1] + " " + t[2] + t[3] + t[4]
    print t[0]
    pass

def p_labeled_statement_2(t):
    'labeled_statement : DEFAULT COLON statement'
    print "p_labeled_statement_2"
    t[0] = t[1] + t[2] + t[3]
    pass

# expression-statement:
def p_expression_statement(t):
    'expression_statement : expression_opt SEMI'
    print "p_expression_statement"
    t[0] = t[1] + t[2]
    print t[0]
    pass

# compound-statement:

def p_compound_statement_1(t):
    'compound_statement : LBRACE declaration_list statement_list RBRACE'
    print "p_compound_statement_1"
    t[0] = t[1] + t[2] + t[3] + t[4]
    print t[0]
    pass

def p_compound_statement_2(t):
    'compound_statement : LBRACE statement_list RBRACE'
    print "p_compound_statement_2"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

def p_compound_statement_3(t):
    'compound_statement : LBRACE declaration_list RBRACE'
    print "p_compound_statement_3"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

def p_compound_statement_4(t):
    'compound_statement : LBRACE RBRACE'
    print "p_compound_statement_4"
    t[0] = t[1] + t[2]
    print t[0]
    pass

# statement-list:

def p_statement_list_1(t):
    'statement_list : statement'
    print "p_statement_list_1"
    t[0] = t[1]
    print t[0]
    pass

def p_statement_list_2(t):
    'statement_list : statement_list statement'
    print "p_statement_list_2"
    t[0] = t[1] + t[2]
    print t[0]
    pass

# selection-statement

def p_selection_statement_1(t):
    'selection_statement : IF LPAREN expression RPAREN statement'
    print "p_selection_statement_1"
    t[0] = t[1] + t[2] + t[3] + t[4] + t[5]
    print t[0]
    pass

def p_selection_statement_2(t):
    'selection_statement : IF LPAREN expression RPAREN statement ELSE statement '
    print "p_selection_statement_2"
    t[0] = t[1] + t[2] + t[3] + t[4] + t[5] + t[6] + t[7]
    print t[0]
    pass

def p_selection_statement_3(t):
    'selection_statement : SWITCH LPAREN expression RPAREN statement '
    print "p_selection_statement_3"
    t[0] = t[1] + t[2] + t[3] + t[4] + t[5]
    print t[0]
    pass

# iteration_statement:

def p_iteration_statement_1(t):
    'iteration_statement : WHILE LPAREN expression RPAREN statement'
    print "p_iteration_statement_1"
    t[0] = t[1] + t[2] + t[3] +t[4] + t[5]
    print t[0]
    pass

def p_iteration_statement_2(t):
    'iteration_statement : FOR LPAREN expression_opt SEMI expression_opt SEMI expression_opt RPAREN statement '
    print "p_iteration_statement_2"
    t[0] = t[1] + t[2] + t[3] +t[4] + t[5] + t[6] + t[7] + t[8] + t[9]
    print t[0]
    pass

# jump_statement:

def p_jump_statement_1(t):
    'jump_statement : CONTINUE SEMI'
    print "p_jump_statement_1"
    t[0] = t[1] + t[2] + "\n"
    print t[0]
    pass

def p_jump_statement_2(t):
    'jump_statement : BREAK SEMI'
    print "p_jump_statement_2"
    t[0] = t[1] + t[2] + "\n"
    print t[0]
    pass

def p_jump_statement_3(t):
    'jump_statement : RETURN expression_opt SEMI'
    print "p_jump_statement_3"
    t[0] = t[1] + " " + t[2] + t[3] + "\n"
    print t[0]
    pass

def p_expression_opt_1(t):
    'expression_opt : empty'
    print "p_expression_opt_1"
    pass

def p_expression_opt_2(t):
    'expression_opt : expression'
    print "p_expression_opt_2"
    t[0] = t[1]
    print t[0]
    pass

# expression:
def p_expression_1(t):
    'expression : assignment_expression'
    print "p_expression_1"
    t[0] = t[1]
    print t[0]
    pass

def p_expression_2(t):
    'expression : expression COMMA assignment_expression'
    print "p_expression_2"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

# assigment_expression:
def p_assignment_expression_1(t):
    'assignment_expression : conditional_expression'
    print "p_assignment_expression_1"
    t[0] = t[1]
    print t[0]
    pass

def p_assignment_expression_2(t):
    'assignment_expression : unary_expression assignment_operator assignment_expression'
    print "p_assignment_expression_2"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

# assignment_operator:
def p_assignment_operator(t):
    '''
    assignment_operator : EQUALS
                        | TIMESEQUAL
                        | DIVEQUAL
                        | MODEQUAL
                        | PLUSEQUAL
                        | MINUSEQUAL
                        | ANDEQUAL
                        | OREQUAL
                        | XOREQUAL
                        '''
    print "p_assignment_operator"
    t[0] = t[1]
    print t[0]
    pass

# conditional-expression
def p_conditional_expression_1(t):
    'conditional_expression : logical_or_expression'
    print "p_conditional_expression_1"
    t[0] = t[1]
    print t[0]
    pass

def p_conditional_expression_2(t):
    'conditional_expression : logical_or_expression CONDOP expression COLON conditional_expression '
    print "p_conditional_expression_2"
    t[0] = t[1] + t[2] + t[3] + t[4] + t[5]
    print t[0]
    pass

# constant-expression

def p_constant_expression(t):
    'constant_expression : conditional_expression'
    print "p_constant_expression"
    t[0] = t[1]
    print t[0]
    pass

# logical-or-expression

def p_logical_or_expression_1(t):
    'logical_or_expression : logical_and_expression'
    print "p_logical_or_expression_1"
    t[0] = t[1]
    print t[0]
    pass

def p_logical_or_expression_2(t):
    'logical_or_expression : logical_or_expression LOR logical_and_expression'
    print "p_logical_or_expression_2"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

# logical-and-expression

def p_logical_and_expression_1(t):
    'logical_and_expression : inclusive_or_expression'
    print "p_logical_and_expression_1"
    t[0] = t[1]
    print t[0]
    pass

def p_logical_and_expression_2(t):
    'logical_and_expression : logical_and_expression LAND inclusive_or_expression'
    print "p_logical_and_expression_2"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

# inclusive-or-expression:

def p_inclusive_or_expression_1(t):
    'inclusive_or_expression : exclusive_or_expression'
    print "p_inclusive_or_expression_1"
    t[0] = t[1]
    print t[0]
    pass

def p_inclusive_or_expression_2(t):
    'inclusive_or_expression : inclusive_or_expression OR exclusive_or_expression'
    print "p_inclusive_or_expression_2"
    t[0] = t[1] + " " + t[2] + " " + t[3]
    print t[0]
    pass

# exclusive-or-expression:

def p_exclusive_or_expression_1(t):
    'exclusive_or_expression :  and_expression'
    print "p_exclusive_or_expression_1"
    t[0] = t[1]
    print t[0]
    pass

def p_exclusive_or_expression_2(t):
    'exclusive_or_expression :  exclusive_or_expression XOR and_expression'
    print "p_exclusive_or_expression_2"
    t[0] = t[1] + " " + t[2] + " " + t[3]
    print t[0]
    pass

# AND-expression

def p_and_expression_1(t):
    'and_expression : equality_expression'
    print "p_and_expression_1"
    t[0] = t[1]
    print t[0]
    pass

def p_and_expression_2(t):
    'and_expression : and_expression AND equality_expression'
    print "p_and_expression_2"
    t[0] = t[1] + " " + t[2] + " " + t[3]
    print t[0]
    pass


# equality-expression:
def p_equality_expression_1(t):
    'equality_expression : relational_expression'
    print "p_equality_expression_1"
    t[0] = t[1]
    print t[0]
    pass

def p_equality_expression_2(t):
    'equality_expression : equality_expression EQ relational_expression'
    print "p_equality_expression_2"
    t[0] = t[1] + " " + t[2] + " " + t[3]
    print t[0]
    pass

def p_equality_expression_3(t):
    'equality_expression : equality_expression NE relational_expression'
    print "p_equality_expression_3"
    t[0] = t[1] + " " + t[2] + " " + t[3]
    print t[0]
    pass

# relational-expression:
def p_relational_expression_1(t):
    'relational_expression : shift_expression'
    print "p_relational_expression_1"
    t[0] = t[1]
    print t[0]
    pass

def p_relational_expression_2(t):
    'relational_expression : relational_expression LT shift_expression'
    print "p_relational_expression_2"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

def p_relational_expression_3(t):
    'relational_expression : relational_expression GT shift_expression'
    print "p_relational_expression_3"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

def p_relational_expression_4(t):
    'relational_expression : relational_expression LE shift_expression'
    print "p_relational_expression_4"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

def p_relational_expression_5(t):
    'relational_expression : relational_expression GE shift_expression'
    print "p_relational_expression_5"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass
    
# shift-expression

def p_shift_expression_1(t):
    'shift_expression : additive_expression'
    print "p_shift_expression_1"
    t[0] = t[1]
    print t[0]
    pass
    
# additive-expression

def p_additive_expression_1(t):
    'additive_expression : multiplicative_expression'
    print "p_additive_expression_1"
    t[0] = t[1]
    print t[0]
    pass

def p_additive_expression_2(t):
    'additive_expression : additive_expression PLUS multiplicative_expression'
    print "p_additive_expression_2"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

def p_additive_expression_3(t):
    'additive_expression : additive_expression MINUS multiplicative_expression'
    print "p_additive_expression_3"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

def p_additive_expression_4(t):
    'additive_expression : additive_expression JPLUS multiplicative_expression'
    print "p_additive_expression_4"
    t[0] = t[1] + ".adder(" + t[3] + ")"
    print t[0]
    pass
 
def p_additive_expression_5(t):
    'additive_expression : additive_expression JMINUS multiplicative_expression'
    print "p_additive_expression_5"
    t[0] = t[1] + ".subtractor(" + t[3] + ")"
    print t[0]
    pass
def p_additive_expression_5(t):
    'additive_expression : additive_expression UNION multiplicative_expression'
    print "p_additive_expression_5"
    t[0] = t[1] + ".union(" + t[3] + ")"
    print t[0]
    pass
 
def p_additive_expression_6(t):
    'additive_expression : additive_expression INTERSECTION multiplicative_expression'
    print "p_additive_expression_6"
    t[0] = t[1] + ".intersect(" + t[3] + ")"
    print t[0]
    pass
# multiplicative-expression

def p_multiplicative_expression_1(t):
    'multiplicative_expression : cast_expression'
    print "p_multiplicative_expression_1"
    t[0] = t[1]
    print t[0]
    pass

def p_multiplicative_expression_2(t):
    'multiplicative_expression : multiplicative_expression TIMES cast_expression'
    print "p_multiplicative_expression_2"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

def p_multiplicative_expression_3(t):
    'multiplicative_expression : multiplicative_expression DIVIDE cast_expression'
    print "p_multiplicative_expression_3"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

def p_multiplicative_expression_4(t):
    'multiplicative_expression : multiplicative_expression MOD cast_expression'
    print "p_multiplicative_expression_4"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

# cast-expression:

def p_cast_expression_1(t):
    'cast_expression : unary_expression'
    print "p_cast_expression_1"
    t[0] = t[1]
    print t[0]
    pass

# unary-expression:
def p_unary_expression_1(t):
    'unary_expression : postfix_expression'
    print "p_unary_expression_1"
    t[0] = t[1]
    print t[0]
    pass

def p_unary_expression_2(t):
    'unary_expression : PLUSPLUS unary_expression'
    print "p_unary_expression_2"
    t[0] = t[1] + t[2]
    print t[0]
    pass

def p_unary_expression_3(t):
    'unary_expression : MINUSMINUS unary_expression'
    print "p_unary_expression_3"
    t[0] = t[1] + t[2]
    print t[0]
    pass

def p_unary_expression_4(t):
    'unary_expression : unary_operator cast_expression'
    print "p_unary_expression_4"
    t[0] = t[1] + t[2]
    print t[0]
    pass
    
#unary-operator
def p_unary_operator(t):
    '''unary_operator : AND
                    | TIMES
                    | PLUS 
                    | MINUS
                    | NOT
                    | LNOT '''
    print "p_unary_operator"
    t[0] = t[1]
    print t[0]
    pass
def p_postfix_expression_1(t):
    'postfix_expression : primary_expression'
    print "p_postfix_expression_1"
    t[0] = t[1]
    print t[0]
    pass

def p_postfix_expression_2(t):
    'postfix_expression : postfix_expression LBRACKET expression RBRACKET'
    print "p_postfix_expression_2"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

def p_postfix_expression_3(t):
    'postfix_expression : postfix_expression LPAREN argument_expression_list RPAREN'
    print "p_postfix_expression_3"
    t[0] = t[1] + t[2] + t[3] + t[4]
    print t[0]
    pass

def p_postfix_expression_4(t):
    'postfix_expression : postfix_expression LPAREN RPAREN'
    print "p_postfix_expression_4"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

def p_postfix_expression_5(t):
    'postfix_expression : postfix_expression PERIOD ID'
    print "p_postfix_expression_5"
    t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass
    
def p_postfix_expression_6(t):
    'postfix_expression : postfix_expression PLUSPLUS'
    print "p_postfix_expression_6"
    t[0] = t[1] + t[2]
    print t[0]
    pass

def p_postfix_expression_7(t):
    'postfix_expression : postfix_expression MINUSMINUS'
    print "p_postfix_expression_7"
    t[0] = t[1] + t[2]
    print t[0]
    pass
    
# primary-expression:
def p_primary_expression(t):
    '''primary_expression :  ID
                        |  NCONST
                        |  SCONST
                        |  LPAREN expression RPAREN'''
    print "p_primary_expression"
    if len(t)>2:
        t[0] = t[1] + t[2] + t[3]
    else:
        t[0] = t[1]
    print t[0]
    pass

# argument-expression-list:
def p_argument_expression_list(t):
    '''argument_expression_list :  assignment_expression
                              |  argument_expression_list COMMA assignment_expression'''
    print "p_argument_expression_list"
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = t[1] + t[2] + t[3]
    print t[0]
    pass

def p_empty(t):
    'empty : '
    print "p_empty"
    print t[0]
    pass


def p_error(p):
    if p:
        #print("Syntax error at '%s'" % p.value)
        raise Exception("Syntax error at '%s'" % p.value)
    else:
        #print("Syntax error at EOF")
        raise Exception("Syntax error at EOF")
        
yacc.yacc(method='LALR')