class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        return self.check(s, dict)
        
    def check(self, s, dict):
        dp = [False] * (len(s)+1)
    
        index = 0
        dp[0] = (s[0] in dict)
        dp[-1] = True
        for c in s:
            for str in dict:
                if str.endswith(c) and index > len(str)-2:
                    dp[index] = dp[index-len(str)]
                if dp[index]:
                    break
            index+=1
    
        return dp[len(s)-1]

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