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

def decimalToHexOrBinary(decimal, base, numBit):
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
        expression += "Diversion by " + str(base) + ": " + str(num) + "\tQuotient: " + str(quotient) + "\treminder: " + str(reminder) + "\n"
        num = quotient
    print "The result of converting decimal number", str(decimal), "to base", str(base), "is:", result
    print expression
    if base == 2 and numBit != False:
        if numBit == 0:
            result = addZeros(result, checkBitsNeeded(result))
        else:
            result = addZeros(result, numBit)
        
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
    if(bits != 0):
        result = zeros + number
        # print "After add zeros:", result
    else:
        result = number + ((23 - len(number)) * "0")
    return result 

# def addZeros(*args):
#     zeros = (args[1] - len(args[0]) * "0"
#     if(len(args) > 2):
#         result = args[0] + zeros
#     else:
#         result = zeros + args[0]
#     return result

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

def twosComplement(number, bit):
    posNum = abs(number)
    posNumInBin = decimalToHexOrBinary(posNum, 2, bit)
    print number, "to positive is:",posNumInBin
    print posNumInBin,"inverted to:",invertBits(posNumInBin)
    #[-len(posNumInBin):] this is aimed to reduced the bits overflow
    #for example 0's twoscomplement is 10000, where we only have for bits, so get rid of first 1
    result = binaryAdd(invertBits(posNumInBin), "1")[-len(posNumInBin):]
    return result

def fractionalToBinary(number, precision):
    result = "0."
    num = number
    while num != 0 and precision != 0:
        intPart = int(num * 2)
        num = num * 2 - intPart
        print intPart, "+", num
        result += str(intPart)
        precision -= 1
    print "The Fractional part to Binary is: ",result
    return result

def calExponent(number):
    if(number[0] == "1"):
        result = number.index(".") - 1
    else:
        result = 1
        firstOne = False
        for i in number:
            if(not firstOne):
                if(i == "1"):
                    firstOne = True
                else:
                    result -= 1
    print "Exponent is: ",result
    return result

def calMantissa(number, exponent):
    if(number[0] == "1"):
        notNormalizedMantissa = number[0] + "." \
                            + number[1:-(len(number) - exponent) + 1] \
                            + number[exponent + 2:]
    else:
        notNormalizedMantissa = number[abs(exponent) + 2] + "." + number[abs(exponent) + 2:]
    return notNormalizedMantissa

def normalizeMantissa(number):
    num = number[2:]
    num = addZeros(num, 0)
    # print "normalizeMantissa:",num
    return num

def ieee754(number, precission):
    num = abs(number)
    if number != num:
        sign = "1"
    else:
        sign = "0"
    intPart, fractional = int(num), num - int(num)
    intPart = decimalToHexOrBinary(intPart, 2, False)
    fractional = fractionalToBinary(fractional, precission)
    posBeforeNormalize = intPart + fractional[1:]
    print posBeforeNormalize
    unadjustedExponent = calExponent(posBeforeNormalize)
    exponent = decimalToHexOrBinary(unadjustedExponent + 127, 2, 8)
    # notNormalizedMantissa = posBeforeNormalize[0] + "." \
    #                         + posBeforeNormalize[1:-(len(posBeforeNormalize) - unadjustedExponent) + 1] \
    #                         + posBeforeNormalize[unadjustedExponent + 2:]
    notNormalizedMantissa = calMantissa(posBeforeNormalize, unadjustedExponent)
    mantissa = normalizeMantissa(notNormalizedMantissa)

    print "sign:", sign, "exponent:", exponent, "mantissa:", mantissa
    print number, "to IEEE 754: ", sign,"-", exponent,"-", mantissa
    return sign + exponent + mantissa

def main():
    # octalOrBinaryToDecimal("01110110010110101", 2)
    # decimalToHexOrBinary(octalOrBinaryToDecimal("0175423", 8), 16, 0)
    # decimalToHexOrBinary(59736, 16, 0)
    # print binaryAdd("100", "1")
    # decimalToHexOrBinary(13, 2, 0)
    # print invertBits("10010")
    # twos = twosComplement(-5763292, 24)
    # print twos
    # octalOrBinaryToDecimal(twos, 2)
    print ieee754(-312.3125, 100)
    print ieee754(0.0390625, 29)
    decimalToHexOrBinary(octalOrBinaryToDecimal(ieee754(0.0390625, 29), 2), 16, 0)
    # fractionalToBinary(0.3125)


if __name__ == "__main__":
    main()
