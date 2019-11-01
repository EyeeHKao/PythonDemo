#!/usr/bin/python3
import re

#regex express match method1: compile() + match()/search()/findall()
s1 = "I am a baby"
p_m = re.compile(r'I')
print(p_m.match(s1))	#从开头处查找，返回一个匹配对象或者None

s2 = "I am a baby and a dad"
p_s = re.compile('a')	#在字符串中查找第一个符合的，并返回一个匹配对象
print(p_s.search(s2))
	
s3 = "Tina is a good girl, she is cool, clever, and so on..."
p_f = re.compile(r'\w*oo\w*')
print(p_f.findall(s3))	#查找所有包含'OO'在内的单词, 返回一个列表

#regex express match method2: direct use match/search/findall
print(re.match(r'I', s1))
print(re.search(r'i', s2, re.I))
print(re.findall(r'\w*oo\w*', s3))


#match object atribute: group()/start()/end()/span()
#match()
print(re.match(r'com', 'Comwww.runcomoob', re.I).group())
print(re.match(r'com', 'Comwww.runcomoob', re.I).start())
print(re.match(r'com', 'Comwww.runcomoob', re.I).end())
print(re.match(r'com', 'Comwww.runcomoob', re.I).span())
#search()
print(re.search(r'www', 'Comwww.runcomoob').group())
print(re.search(r'www', 'Comwww.runcomoob').start())
print(re.search(r'www', 'Comwww.runcomoob').end())
print(re.search(r'www', 'Comwww.runcomoob').span())

#　greedy match and noe-greedy match
print(re.findall(r"a(\d+?)", "a23456b"))	#非贪婪匹配，打印['2']
print(re.findall(r"a(\d+)", 'a23456b'))	#贪婪匹配，打印['23456']





