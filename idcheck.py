#!/usr/bin/python
# -*- coding: utf-8 -*-
import string

standardhead = string.letters + '_'
nums = string.digits

print 'testees must be at least 2 chars'
myInput = raw_input('identifier to test?')

if len(myInput)>1:
    if myInput[0] not in standardhead:
        print '''invalid:first symbol must be alphabetic'''
    else:
        for otherChar in myInput[1:]:
            if otherChar not in standardhead+nums:
                print '''invalid:remainint symbols
                        must be alphanumeric'''
                break
        print "okay as an identifier"
else:
    print "testees must be at least 2 chars"