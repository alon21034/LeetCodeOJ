class Solution:
    
    def isInt(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for x in tokens:
            if self.isInt(x):
                stack.append(int(x))
            else:
                buf2 = stack.pop()
                buf1 = stack.pop()
                if x == '+':
                    buf1 = buf1 + buf2
                elif x == '-':
                    buf1 = buf1 - buf2
                elif x == '*':
                    buf1 = buf1 * buf2
                elif x == '/':
                    buf1 = int(float(buf1)/buf2)
                stack.append(buf1)
        return stack.pop()