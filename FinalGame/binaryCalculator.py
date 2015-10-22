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
    binary = convertToBinary(number)
    binary = "1" + binary 
    return binary
    
def convertToTwosComplement(number):
    binary = convertToBinary(number)
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

def runMenu():
    number = int(input("Enter an decimal integer to be converted into binary: "))
    if number > 0:
        return convertToBinary(number)
    elif number < 0:
        while True:
            print(" 0. Nevermind \n 1. Sign and Magnitude \n 2. Two's Complement")        
            choice = int(input("What method of conversion would you like to use? "))
            if choice == 0:
                break
            elif choice == 1:
                return convertToSignMagnitude(number*-1)
                break
            elif choice == 2:
                return convertToTwosComplement(number*-1)
                break
            else:
                print("There is no such option. \n")

while True:
    result = runMenu()
    if result == 0:
        print("Bye.")
        break
    else:
        print("The binary number is ", result)
