import math
def octalOrBinaryToDecimal(number, base):
    result = 0
    count = len(number) - 1
    expression = "The process is:\n"
    for i in number:
        result += int(i) * pow(base, count)
        expression += "(" + str(i) + " * " + str(base) + "^" + str(count) + ") + "
        count -= 1
    print "The result of converting", str(number), "with a base of", str(base), "to decimal is:", int(result)
    print expression[:-3]
    return int(result)

def decimalToHexOrBinary(decimal, base):
    num = decimal
    quotient = -1
    reminder = -1
    result = ""
    expression = "The process is:\n"
    hexList = list("0123456789ABCDEF")
    while quotient != 0:
        quotient = int(num / base)
        reminder = int(num % base)
        result = hexList[reminder] + result
        expression += "Diversion by 16: " + str(num) + "\tQuotient: " + str(quotient) + "\treminder: " + str(reminder) + "\n"
        num = quotient
    print "The result of converting decimal number", str(decimal), "to base", str(base), "is:", result
    print expression
    if base == 2:
        result = addZeros(result, checkBitsNeeded(result))
    return result

def checkBitsNeeded(number):
    leastBits = 4
    enough = False
    for i in range(2, 8):
        if(not enough):
            if(pow(2, i) > len(number)):
                leastBits = pow(2, i)
                enough = True
    return leastBits

def addZeros(number, bits):
    zeros = (bits - len(number)) * "0"
    return zeros + number 

def binaryAdd(*args):
    result = "0"
    for i in args:
        result = bin(int(i, 2) + int(result, 2))
    return result[2:]

def invertBits(number):
    num = list(number)
    count = 0
    for i in num:
        if i == "1":
            num[count] = 0 
        else:
            num[count] = 1
        count += 1
    return ''.join(map(str, num))

def twosComplement(number):
    posNum = abs(number)
    posNumInBin = decimalToHexOrBinary(posNum, 2)
    print number, "to positive is:",posNumInBin
    print posNumInBin,"inverted to:",invertBits(posNumInBin)
    #[-len(posNumInBin):] this is aimed to reduced the bits overflow
    #for example 0's twoscomplement is 10000, where we only have for bits, so get rid of first 1
    result = binaryAdd(invertBits(posNumInBin), "1")[-len(posNumInBin):]
    return result


def main():
    octalOrBinaryToDecimal("01110110010110101", 2)
    decimalToHexOrBinary(octalOrBinaryToDecimal("0175423", 8), 16)
    decimalToHexOrBinary(59736, 16)
    print binaryAdd("100", "1")
    decimalToHexOrBinary(13, 2)
    print invertBits("10010")
    print twosComplement(0)

if __name__ == "__main__":
    main()
