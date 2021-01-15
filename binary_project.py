def binary_converter(num, bin):
    '''
    This function has two different modes.
    If you input a positive integer, it returns a string of 1’s and 0’s that encode it in 16-bit binary.
    If you input a 16-bit string of 1’s and 0’s, it will return the positive integer that the string represents.
    If you input a value outside the accepted range, it will return None.
    :param input_value: a positive integer, or a string of 1’s and 0’s
    :return: a string of 1’s and 0’s or a positive integer
    '''
    binary = []
    if num > 65535 or num < 1:
        print('None')
    if bin > 1111111111111111:
        print('None')
    else:
        while num >= 1:
            remainder = num % 2
            num /= 2
            if remainder == 0:
                binary.append(0)
            elif remainder > 0:
                binary.append(1)
        if bin >= 0000000000000000:
            binary_list = ([int(d) for d in str(bin)])
            one_bit = ((binary_list[15]) * 2**0)
            two_bit = ((binary_list[14]) * 2**1)
            three_bit = ((binary_list[13]) * 2**2)
            four_bit = ((binary_list[12]) * 2**3)
            five_bit = ((binary_list[11]) * 2**4)
            six_bit = ((binary_list[10]) * 2**5)
            seven_bit = ((binary_list[9]) * 2**6)
            eight_bit = ((binary_list[8]) * 2**7)
            nine_bit = ((binary_list[7]) * 2**8)
            ten_bit = ((binary_list[6]) * 2**9)
            eleven_bit = ((binary_list[5]) * 2**10)
            twelve_bit = ((binary_list[4]) * 2**11)
            thirteen_bit = ((binary_list[3]) * 2**12)
            fourteen_bit = ((binary_list[2]) * 2**13)
            fifteen_bit = ((binary_list[1]) * 2**14)
            sixteen_bit = ((binary_list[0]) * 2**15)
            res = (one_bit + two_bit + three_bit + four_bit + five_bit + six_bit + seven_bit + eight_bit +
                   nine_bit + ten_bit + eleven_bit + twelve_bit + thirteen_bit + fourteen_bit + fifteen_bit +
                   sixteen_bit)
    while len(binary) != 16:
        binary.append(0)
    binary.reverse()
    print(binary)
    print(res)

def binary_converter_v2(num, comp):
    '''
    This function has two different modes.
    If you input an integer, it returns a string of 1’s and 0’s that encode it in 16-bit binary.
    If you input a 16-bit string of 1’s and 0’s,
    it will return the two’s complement number that the string represents.
    If you input a value outside the accepted range, it will return None.
    :param: input_value: a positive integer, or a string of 1’s and 0’s
    :return: a string of 1’s and 0’s or an integer
    '''
    binary = []
    if num > 65535 or num < 1:
        print('None')
    if comp > 1111111111111111:
        print('None')
    else:
        while num >= 1:
            remainder = num % 2
            num /= 2
            if remainder == 0:
                binary.append(0)
            elif remainder > 0:
                binary.append(1)
        if comp >= 0000000000000000:
            binary_list = ([int(d) for d in str(bin)])
            for x in range(0, 16):
                if binary_list[x] == 0:
                   binary_list[x] = 1
                elif binary_list[x] == 1:
                    binary_list[x] = 0
    while len(binary) != 16:
        binary.append(0)
    binary.reverse()
    print(binary)

print(binary_converter_v2(12,1000000000000001))