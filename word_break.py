class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        dict = self.trim(list(dict))
        return self.check(s, dict)
        
    def check(self, s, dict):
    	if s == '':
    		return True
    	str = ''
    	first = ''
    	for c in s:
    		str += c
    		if str in dict:
    			first = str
    			ret = self.check(s[len(str):], dict)
    			if ret:
    				return True
    	return False
    
    def trim(self, dict):
    	tmp = dict[:]
    	flag = False
    	stack = []
    	for i in range(1, len(dict)):
    		c = dict[i]
    		tmp.remove(c)
    		if self.check(c, tmp):
    			stack+=[c]
    		else:
    			tmp = dict[:]
    	for c in stack:
    		dict.remove(c)
    	return dict