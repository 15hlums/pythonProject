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
            binary_list = ([int(d) for d in str(comp)])
            for x in range(0, 16):
                if binary_list[x] == 0:
                   binary_list[x] = 1
                elif binary_list[x] == 1:
                    binary_list[x] = 0
            if binary_list[15] == 0:
                binary_list[15] = 1
            elif binary_list[15] == 1:
                binary_list[15] = 0
                if binary_list[14] == 0:
                    binary_list[14] = 1
                elif binary_list[14] == 1:
                    binary_list[14] = 0
                    if binary_list[13] == 0:
                        binary_list[13] = 1
                    elif binary_list[13] == 1:
                        binary_list[13] = 0
                        if binary_list[12] == 0:
                            binary_list[12] = 1
                        elif binary_list[12] == 1:
                            binary_list[12] = 0
                            if binary_list[11] == 0:
                                binary_list[11] = 1
                            elif binary_list[11] == 1:
                                binary_list[11] = 0
                                if binary_list[10] == 0:
                                    binary_list[10] = 1
                                elif binary_list[10] == 1:
                                    binary_list[10] = 0
                                    if binary_list[9] == 0:
                                        binary_list[9] = 1
                                    elif binary_list[9] == 1:
                                        binary_list[9] = 0
                                        if binary_list[8] == 0:
                                            binary_list[8] = 1
                                        elif binary_list[8] == 1:
                                            binary_list[8] = 0
                                            if binary_list[7] == 0:
                                                binary_list[7] = 1
                                            elif binary_list[7] == 1:
                                                binary_list[7] = 0
                                                if binary_list[6] == 0:
                                                    binary_list[6] = 1
                                                elif binary_list[6] == 1:
                                                    binary_list[6] = 0
                                                    if binary_list[5] == 0:
                                                        binary_list[5] = 1
                                                    elif binary_list[5] == 1:
                                                        binary_list[5] = 0
                                                        if binary_list[4] == 0:
                                                            binary_list[4] = 1
                                                        elif binary_list[4] == 1:
                                                            binary_list[4] = 0
                                                            if binary_list[3] == 0:
                                                                binary_list[3] = 1
                                                            elif binary_list[3] == 1:
                                                                binary_list[3] = 0
                                                                if binary_list[2] == 0:
                                                                    binary_list[2] = 1
                                                                elif binary_list[2] == 1:
                                                                    binary_list[2] = 0
                                                                    if binary_list[1] == 0:
                                                                        binary_list[1] = 1
                                                                    elif binary_list[1] == 1:
                                                                        binary_list[1] = 0
                                                                        if binary_list[0] == 0:
                                                                            binary_list[0] = 1
                                                                        elif binary_list[0] == 1:
                                                                            binary_list[0] = 0
    while len(binary) != 16:
        binary.append(0)
    binary.reverse()
    print(binary)
    print(binary_list)

def binary_converter_v3(num, comp):
    '''
    This function has two different modes.
    If you input a decimal, it returns a string of 1’s and 0’s that encode it in 16-bit binary.
    If you input a 16-bit string of 1’s and 0’s,
    it will return the two’s complement number that the string represents.
    If you input a value outside the accepted range, it will return None.
    If you put a value that will not perfectly fit into a binary decimal,
    it will round the value down as little as possible.
    It also takes a second input that tells it where the fixed decimal point is located.
    :param: input_value: a positive integer, or a string of 1’s and 0’s
    :param: fixed_position: a positive integer from 0 to 15,
            this indicates which bit the fixed point is found in front of.
            So position 0 would have all bits behind the fixed point
    :return: a number
    '''
    binary = []
    x = divmod(num, 1)
    integer = int(x[0])
    decimal = (x[1])
    if num > 65535 or num < 1:
        print('None')
    else:
        while integer >= 1:
            remainder = integer % 2
            integer /= 2
            if remainder == 0:
                binary.append(0)
            elif remainder > 0:
                binary.append(1)
        binary.reverse()
        binary.append('.')
        while decimal > 0:
            decimal *= 2
            if int(decimal) == 1:
                binary.append(1)
                decimal -= 1
            elif int(decimal) == 0:
                binary.append(0)
        if comp >= 0000000000000000:
            binary_list = ([int(d) for d in str(comp)])
            for x in range(0, 16):
                if binary_list[x] == 0:
                   binary_list[x] = 1
                elif binary_list[x] == 1:
                    binary_list[x] = 0
            if binary_list[15] == 0:
                binary_list[15] = 1
            elif binary_list[15] == 1:
                binary_list[15] = 0
                if binary_list[14] == 0:
                    binary_list[14] = 1
                elif binary_list[14] == 1:
                    binary_list[14] = 0
                    if binary_list[13] == 0:
                        binary_list[13] = 1
                    elif binary_list[13] == 1:
                        binary_list[13] = 0
                        if binary_list[12] == 0:
                            binary_list[12] = 1
                        elif binary_list[12] == 1:
                            binary_list[12] = 0
                            if binary_list[11] == 0:
                                binary_list[11] = 1
                            elif binary_list[11] == 1:
                                binary_list[11] = 0
                                if binary_list[10] == 0:
                                    binary_list[10] = 1
                                elif binary_list[10] == 1:
                                    binary_list[10] = 0
                                    if binary_list[9] == 0:
                                        binary_list[9] = 1
                                    elif binary_list[9] == 1:
                                        binary_list[9] = 0
                                        if binary_list[8] == 0:
                                            binary_list[8] = 1
                                        elif binary_list[8] == 1:
                                            binary_list[8] = 0
                                            if binary_list[7] == 0:
                                                binary_list[7] = 1
                                            elif binary_list[7] == 1:
                                                binary_list[7] = 0
                                                if binary_list[6] == 0:
                                                    binary_list[6] = 1
                                                elif binary_list[6] == 1:
                                                    binary_list[6] = 0
                                                    if binary_list[5] == 0:
                                                        binary_list[5] = 1
                                                    elif binary_list[5] == 1:
                                                        binary_list[5] = 0
                                                        if binary_list[4] == 0:
                                                            binary_list[4] = 1
                                                        elif binary_list[4] == 1:
                                                            binary_list[4] = 0
                                                            if binary_list[3] == 0:
                                                                binary_list[3] = 1
                                                            elif binary_list[3] == 1:
                                                                binary_list[3] = 0
                                                                if binary_list[2] == 0:
                                                                    binary_list[2] = 1
                                                                elif binary_list[2] == 1:
                                                                    binary_list[2] = 0
                                                                    if binary_list[1] == 0:
                                                                        binary_list[1] = 1
                                                                    elif binary_list[1] == 1:
                                                                        binary_list[1] = 0
                                                                        if binary_list[0] == 0:
                                                                            binary_list[0] = 1
                                                                        elif binary_list[0] == 1:
                                                                            binary_list[0] = 0
    add = [0]
    while len(binary) != 17:
        binary = add + binary
    print(binary)
    print(binary_list)

def binary_converter_v4(num, exponent):
    '''
    If you input a 16-bit string of 1’s and 0’s,
    it will return the two’s complement number that the string represents.
    If you input a value outside the accepted range, it will return None.
    If you put a value that will not perfectly fit into a binary decimal,
    it will round the value down as little as possible.
    It also takes a second input that tells it how many bits are used in the exponent.
    It is assumed 1 for the sign bit and the rest for the mantissa.
    :param: input_value a string of 1’s and 0’s
    :param: exponent_bits: a positive integer from 1 to 13, this how many bits are used in the exponent.
            These are always found at the end of the string
    :return: a number
    '''
    if num > 1111111111111111:
        print('None')
    if num >= 0000000000000000:
        binary_list = ([int(d) for d in str(num)])
        for x in range(0, 16, 1):
            if binary_list[x] == 1:
                binary_list[x] = 0
            elif binary_list[x] == 0:
                binary_list[x] = 1
        if binary_list[15] == 0:
            binary_list[15] = 1
        elif binary_list[15] == 1:
            binary_list[15] = 0
            if binary_list[14] == 0:
                binary_list[14] = 1
            elif binary_list[14] == 1:
                binary_list[14] = 0
                if binary_list[13] == 0:
                    binary_list[13] = 1
                elif binary_list[13] == 1:
                    binary_list[13] = 0
                    if binary_list[12] == 0:
                        binary_list[12] = 1
                    elif binary_list[12] == 1:
                        binary_list[12] = 0
                        if binary_list[11] == 0:
                            binary_list[11] = 1
                        elif binary_list[11] == 1:
                            binary_list[11] = 0
                            if binary_list[10] == 0:
                                binary_list[10] = 1
                            elif binary_list[10] == 1:
                                binary_list[10] = 0
                                if binary_list[9] == 0:
                                    binary_list[9] = 1
                                elif binary_list[9] == 1:
                                    binary_list[9] = 0
                                    if binary_list[8] == 0:
                                        binary_list[8] = 1
                                    elif binary_list[8] == 1:
                                        binary_list[8] = 0
                                        if binary_list[7] == 0:
                                            binary_list[7] = 1
                                        elif binary_list[7] == 1:
                                            binary_list[7] = 0
                                            if binary_list[6] == 0:
                                                binary_list[6] = 1
                                            elif binary_list[6] == 1:
                                                binary_list[6] = 0
                                                if binary_list[5] == 0:
                                                    binary_list[5] = 1
                                                elif binary_list[5] == 1:
                                                    binary_list[5] = 0
                                                    if binary_list[4] == 0:
                                                        binary_list[4] = 1
                                                    elif binary_list[4] == 1:
                                                        binary_list[4] = 0
                                                        if binary_list[3] == 0:
                                                            binary_list[3] = 1
                                                        elif binary_list[3] == 1:
                                                            binary_list[3] = 0
                                                            if binary_list[2] == 0:
                                                                binary_list[2] = 1
                                                            elif binary_list[2] == 1:
                                                                binary_list[2] = 0
                                                                if binary_list[1] == 0:
                                                                    binary_list[1] = 1
                                                                elif binary_list[1] == 1:
                                                                    binary_list[1] = 0
                                                                    if binary_list[0] == 0:
                                                                        binary_list[0] = 1
                                                                    elif binary_list[0] == 1:
                                                                        binary_list[0] = 0

        exponant_list = []
        for x in range(15, 15 - exponent, -1):
            exponant_list.append(binary_list[x])
        exponant_list.reverse()

        for x in range(15, 15 - exponent, -1):
            binary_list.pop(x)

        shift = 0
        power = 0

        for x in range(exponent - 1, -1, -1):
            bit = ((exponant_list[x]) * 2 ** power)
            shift += bit
            power += 1

        decimal_place = []

        for x in range(15 - exponent, shift, -1):
            decimal_place.append(binary_list[x])
            binary_list.pop(x)
        decimal_place.reverse()

        dec_power = -1
        dec_res = 0

        for x in range(0, len(decimal_place), 1):
            dec = ((decimal_place[x]) * 2 ** dec_power)
            dec_res += dec
            dec_power -= 1

        int_power = 0
        int_res = 0

        for x in range(len(binary_list) - 1, -1, -1):
            integer = ((binary_list[x]) * 2 ** int_power)
            int_res += integer
            int_power += 1

        res = int_res + dec_res
        print(res)

def binary_normalisation(num, exponent):
    '''
    This function takes a given 16-bit binary string and normalised it.
    It also takes a second input that tells it how many bits are used in the exponent.
    It is assumed 1 for the sign bit and the rest for the mantissa.
    :param: input_value a string of 1’s and 0’s
    :param: exponent_bits: a positive integer from 1 to 13, this how many bits are used in the exponent.
            These are always found at the end of the string
    :return: a normalized string of 1’s and 0’s
    '''
    if num > 1111111111111111:
        print('None')
    else:
        binary_list = ([int(d) for d in str(num)])

        exponant_binary = []

        for x in range(len(binary_list) - 1, len(binary_list) - exponent - 1, -1):
            exponant_binary.append(binary_list[x])
            binary_list.pop(x)
        exponant_binary.reverse()

        exponant_shift = 0

        for x in range(1, 16, 1):
            if binary_list[1] == 0:
                binary_list.pop(1)
                exponant_shift += 1
            elif binary_list[1] == 1:
                 break

        for x in range(0, exponant_shift, 1):
            binary_list.append(0)

        power = 0
        exponent_res = 0

        for x in range(len(exponant_binary) - 1, 0, -1):
                bit = ((exponant_binary[x]) * 2 ** power)
                exponent_res += bit
                power += 1

        exponent_res -= exponant_shift

        exp_bin_final = []

        while exponent_res >= 1:
            remainder = exponent_res % 2
            exponent_res /= 2
            if remainder == 0:
                exp_bin_final.append(0)
            elif remainder > 0:
                exp_bin_final.append(1)

        while len(exp_bin_final) != len(exponant_binary):
            exp_bin_final.append(0)
        exp_bin_final.reverse()

        res = binary_list + exp_bin_final
        print(res)