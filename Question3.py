#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Note that an empty string is also considered valid.



class Solution:
    def isValid(self, s: str) -> bool:
        
        def is_matched_parenthesis(left, right):
            
            return left == '(' and right == ')' or left == '{' and right == '}' or left == '[' and right == ']'
        
        stack = []
        
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if not stack or not is_matched_parenthesis(stack[-1], ch):                
                    return False                    
                else:                
                    stack.pop()
        Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

        return not stack
