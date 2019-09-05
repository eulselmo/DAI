#!/usr/bin/env python
#-*-coding:utf-8-*-

def eratostenes(num, print_nums=False)
	if num < 3:
        	raise Exception, 'Number is too small'
	full_nums = range(num)[1:] + [num]
	primes = [False] + [True]*(num - 1)
    	for i in range(num):
        	if primes[i]:
           	 if print_nums:
                	print full_nums[i]
            	 inc = full_nums[i]
           	 cursor = i + inc
            	 if cursor > num:
                	break
            	 while cursor < num:
                	primes[cursor] = False
                	cursor += inc
    	return [full_nums[j] for j in range(num) if primes[j
