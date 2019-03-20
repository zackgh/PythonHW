class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items

"""
Binary
"""

def div_by_two(dec_num):
    s = Stack()
    bin_num = ''
    while dec_num>0:
        remainder = dec_num%2
        dec_num=dec_num//2
        s.push(remainder)
    while not s.is_empty():
        bin_num+=str(s.pop())
    return bin_num


print(div_by_two(256))

"""
loop through a string and push contents Character by character
onto a stack
"""

def rev_string(input_str):
    s = Stack()
    index = 0
    while index in range(len(input_str)):
        s.push(input_str[index])
        index+=1
    rev_str=''
    while not s.is_empty():
        rev_str += s.pop()
    return rev_str

print(rev_string('YOB'))

"""
using stack to check balance of parenthesis 
"""

# first cewrsion has flaws 

def is_match(p1,p2):
    if p1 =='(' and p2 == ')':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    else:
        return False
    
def is_paren_balanced(paren_string):
    index = 0
    is_balanced=True
    s = Stack()
    if paren_string == '':
       is_balanced=False
       return False
    elif paren_string[-1] in '([(':
        is_balanced = False
        return False
    else:
        while index<len(paren_string) and is_balanced==True:
            if paren_string[index] in '([{':
                s.push(paren_string[index])
            else:
                if s.is_empty():
                    is_balanced = False
                    return False
                elif is_match(s.pop(),paren_string[index]):
                    is_balanced = True
                else:
                    is_balanced == False
                    return False
            index += 1
    if s.is_empty() and is_balanced == True:
        return True 
        
       
    
print(is_paren_balanced('[]'))
print(is_paren_balanced('[{()}]'))
print(is_paren_balanced('())'))























