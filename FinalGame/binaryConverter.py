# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:33:28 2015

@author: Aps
"""
def reverseString(string):
    result = ""
    for ch in string:
        result = ch + result
    return result
    
def convertToBinary(number):
    binary = ""
    while number != 0:
        binary = str(number % 2) + binary  
        number = number // 2
    return binary
   
def convertToSignMagnitude(number):
    binary = convertToBinary(abs(number))
    binary = "1" + binary 
    return binary
    
def convertToTwosComplement(number):
    binary = convertToBinary(abs(number))
    invertedBinary = ""
    tempString = ""
    s = ""
    i = 0
    #inverting the 1s and 0s
    for ch in binary:
        if ch == "1":
            invertedBinary += "0"
        else:
            invertedBinary += "1"
    
    #temporarily reversing the string  
    tempString = reverseString(invertedBinary)        
    #add 1
    for ch in tempString:
        if ch == "0":
            s = list(tempString)
            s[i] = "1"
            tempString = "".join(s)
            zeros = ""            
            for n in range(0,i):
                zeros += "0"
            tempString = zeros + tempString[i:]
            break
        i += 1
    
    #reversing the string back
    final = reverseString(tempString)
    #adding a 1 in front to make it negative
    if final[0] == "0":
        final = "1" + final
        
    return final