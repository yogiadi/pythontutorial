```python
code=compile('a + 5','file.py','eval')
a=5
eval(code)
```




    10




```python
import parser
st=parser.expr('a + 5')
code= st.compile('file.py')
a=5
eval(code)
```




    10




```python
import parser
def load_suite(source_string):
    st = parser.suite(source_string)
    return st, st.compile()
def load_expression(source_string):
    st=parser.expr(source_string)
    return st, st.compile()
```


```python
import ast
class RewriteName(ast.NodeTransformer):
    def visit_Name(self,node):
        return Subscript(
        value=Name(id='data', ctx=Load()),
        slice=Index(value=Constant(value=nodde.id)),
        ctx=node.ctx
        )
```


```python
import symtable
table=symtable.symtable("def some_func():    x=5","string","exec")
table.lookup("some_func").is_namespace()
```




    True




```python
from tokenize import tokenize , untokenize , NUMBER , STRING , NAME , OP
from io import BytesIO
def decistmt(s):
    result = []
    g=tokenize(BytesIO(s.encode('utf-8')).readline)
    for toknum, tokval,_,_,_ in g:
        if toknum == NUMBER and '.' in tokval:
            result.extend([
                (NAME, 'Decimal'),
                (OP,'('),
                (STRING, repr(tokval)),
                (OP,')')
            ])
        else:
            result.append((toknum, tokval))
    return untokenize(result).decode('utf-8')
```


```python
!python -m tokenize hello.py
```

    0,0-0,0:            ENCODING       'utf-8'        
    1,0-1,3:            NAME           'def'          
    1,4-1,13:           NAME           'say_hello'    
    1,13-1,14:          OP             '('            
    1,14-1,15:          OP             ')'            
    1,15-1,16:          OP             ':'            
    1,16-1,17:          NEWLINE        '\n'           
    2,0-2,4:            INDENT         '    '         
    2,4-2,9:            NAME           'print'        
    2,9-2,10:           OP             '('            
    2,10-2,25:          STRING         "'Hello, World!'"
    2,25-2,26:          OP             ')'            
    2,26-2,27:          NEWLINE        '\n'           
    3,0-3,0:            DEDENT         ''             
    3,0-3,9:            NAME           'say_hello'    
    3,9-3,10:           OP             '('            
    3,10-3,11:          OP             ')'            
    3,11-3,12:          NEWLINE        ''             
    4,0-4,0:            ENDMARKER      ''             
    


```python
!python -m tokenize -e hello.py
```

    0,0-0,0:            ENCODING       'utf-8'        
    1,0-1,3:            NAME           'def'          
    1,4-1,13:           NAME           'say_hello'    
    1,13-1,14:          LPAR           '('            
    1,14-1,15:          RPAR           ')'            
    1,15-1,16:          COLON          ':'            
    1,16-1,17:          NEWLINE        '\n'           
    2,0-2,4:            INDENT         '    '         
    2,4-2,9:            NAME           'print'        
    2,9-2,10:           LPAR           '('            
    2,10-2,25:          STRING         "'Hello, World!'"
    2,25-2,26:          RPAR           ')'            
    2,26-2,27:          NEWLINE        '\n'           
    3,0-3,0:            DEDENT         ''             
    3,0-3,9:            NAME           'say_hello'    
    3,9-3,10:           LPAR           '('            
    3,10-3,11:          RPAR           ')'            
    3,11-3,12:          NEWLINE        ''             
    4,0-4,0:            ENDMARKER      ''             
    


```python
import tokenize 
with tokenize.open('hello.py') as f:
    tokens = tokenize.generate_tokens(f.readline)
    for token in tokens:
        print(token)
```

    TokenInfo(type=1 (NAME), string='def', start=(1, 0), end=(1, 3), line='def say_hello():\n')
    TokenInfo(type=1 (NAME), string='say_hello', start=(1, 4), end=(1, 13), line='def say_hello():\n')
    TokenInfo(type=53 (OP), string='(', start=(1, 13), end=(1, 14), line='def say_hello():\n')
    TokenInfo(type=53 (OP), string=')', start=(1, 14), end=(1, 15), line='def say_hello():\n')
    TokenInfo(type=53 (OP), string=':', start=(1, 15), end=(1, 16), line='def say_hello():\n')
    TokenInfo(type=4 (NEWLINE), string='\n', start=(1, 16), end=(1, 17), line='def say_hello():\n')
    TokenInfo(type=5 (INDENT), string='    ', start=(2, 0), end=(2, 4), line="    print('Hello, World!')\n")
    TokenInfo(type=1 (NAME), string='print', start=(2, 4), end=(2, 9), line="    print('Hello, World!')\n")
    TokenInfo(type=53 (OP), string='(', start=(2, 9), end=(2, 10), line="    print('Hello, World!')\n")
    TokenInfo(type=3 (STRING), string="'Hello, World!'", start=(2, 10), end=(2, 25), line="    print('Hello, World!')\n")
    TokenInfo(type=53 (OP), string=')', start=(2, 25), end=(2, 26), line="    print('Hello, World!')\n")
    TokenInfo(type=4 (NEWLINE), string='\n', start=(2, 26), end=(2, 27), line="    print('Hello, World!')\n")
    TokenInfo(type=6 (DEDENT), string='', start=(3, 0), end=(3, 0), line='say_hello()')
    TokenInfo(type=1 (NAME), string='say_hello', start=(3, 0), end=(3, 9), line='say_hello()')
    TokenInfo(type=53 (OP), string='(', start=(3, 9), end=(3, 10), line='say_hello()')
    TokenInfo(type=53 (OP), string=')', start=(3, 10), end=(3, 11), line='say_hello()')
    TokenInfo(type=4 (NEWLINE), string='', start=(3, 11), end=(3, 12), line='')
    TokenInfo(type=0 (ENDMARKER), string='', start=(4, 0), end=(4, 0), line='')
    


```python
import tokenize 
with open('hello.py','rb') as f:
    tokens = tokenize.tokenize(f.readline)
    for token in tokens:
        print(token)
```

    TokenInfo(type=57 (ENCODING), string='utf-8', start=(0, 0), end=(0, 0), line='')
    TokenInfo(type=1 (NAME), string='def', start=(1, 0), end=(1, 3), line='def say_hello():\n')
    TokenInfo(type=1 (NAME), string='say_hello', start=(1, 4), end=(1, 13), line='def say_hello():\n')
    TokenInfo(type=53 (OP), string='(', start=(1, 13), end=(1, 14), line='def say_hello():\n')
    TokenInfo(type=53 (OP), string=')', start=(1, 14), end=(1, 15), line='def say_hello():\n')
    TokenInfo(type=53 (OP), string=':', start=(1, 15), end=(1, 16), line='def say_hello():\n')
    TokenInfo(type=4 (NEWLINE), string='\n', start=(1, 16), end=(1, 17), line='def say_hello():\n')
    TokenInfo(type=5 (INDENT), string='    ', start=(2, 0), end=(2, 4), line="    print('Hello, World!')\n")
    TokenInfo(type=1 (NAME), string='print', start=(2, 4), end=(2, 9), line="    print('Hello, World!')\n")
    TokenInfo(type=53 (OP), string='(', start=(2, 9), end=(2, 10), line="    print('Hello, World!')\n")
    TokenInfo(type=3 (STRING), string="'Hello, World!'", start=(2, 10), end=(2, 25), line="    print('Hello, World!')\n")
    TokenInfo(type=53 (OP), string=')', start=(2, 25), end=(2, 26), line="    print('Hello, World!')\n")
    TokenInfo(type=4 (NEWLINE), string='\n', start=(2, 26), end=(2, 27), line="    print('Hello, World!')\n")
    TokenInfo(type=6 (DEDENT), string='', start=(3, 0), end=(3, 0), line='say_hello()')
    TokenInfo(type=1 (NAME), string='say_hello', start=(3, 0), end=(3, 9), line='say_hello()')
    TokenInfo(type=53 (OP), string='(', start=(3, 9), end=(3, 10), line='say_hello()')
    TokenInfo(type=53 (OP), string=')', start=(3, 10), end=(3, 11), line='say_hello()')
    TokenInfo(type=4 (NEWLINE), string='', start=(3, 11), end=(3, 12), line='')
    TokenInfo(type=0 (ENDMARKER), string='', start=(4, 0), end=(4, 0), line='')
    


```python
import compileall
compileall.compile_dir('Lib/',force=True)
import re
compileall.compile_dir('Lib/',rx=re.compile(r'[/\\][.]svn'),force=True)
import pathlib
compileall.compile_dir(pathlib.Path('Lib/'), force=True)
```

    Listing 'Lib/'...
    Can't list 'Lib/'
    Listing 'Lib/'...
    Can't list 'Lib/'
    Listing 'Lib'...
    Can't list 'Lib'
    




    True




```python
def myfunc(alist):
    return len(alist)
```


```python
import dis
dis.dis(myfunc)
```

      2           0 LOAD_GLOBAL              0 (len)
                  2 LOAD_FAST                0 (alist)
                  4 CALL_FUNCTION            1
                  6 RETURN_VALUE
    


```python
bytecode = dis.Bytecode(myfunc)
for instr in bytecode:
    print(instr.opname)
```

    LOAD_GLOBAL
    LOAD_FAST
    CALL_FUNCTION
    RETURN_VALUE
    


```python
import pickle
a = (1, 2)
file_Name = "x.pickle"
fileObject = open(file_Name,'wb') 
pickle.dump(a,fileObject)   
fileObject.close()
```


```python
!python -m pickle x.pickle
```

    (1, 2)
    


```python
!python -m pickletools x.pickle
```

        0: \x80 PROTO      3
        2: K    BININT1    1
        4: K    BININT1    2
        6: \x86 TUPLE2
        7: q    BINPUT     0
        9: .    STOP
    highest protocol among opcodes = 2
    


```python

```
