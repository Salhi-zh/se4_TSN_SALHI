import struct

def float_to_bin(f):
    packed = struct.pack('>d', f)
    integers = [c for c in packed]
    binaries = [bin(i).replace('0b', '').rjust(8,'0') for i in integers]
    full_binary = ''.join(binaries)


    sign = full_binary[0]
    exponent = full_binary[1: 12]
    mantissa = full_binary[12:]
    
    return sign, exponent, mantissa, full_binary



def print_float_representation(f):
    """Print the IEEE 754 representation of a float"""
    sign, exponent, mantissa, full_binary = float_to_bin(f)
    
    print(f"Number: {f}")
    print(f"Sign bit (1 bit): {sign}")
    print(f"Exponent bits (11 bits): {exponent}")
    print(f"Mantissa bits (52 bits): {mantissa}")
    print(f"Full binary representation (64 bits): {full_binary}")
    
    
    sign_value = -1 if sign == '1' else 1
    exponent_value = int(exponent, 2) - 1023
    mantissa_value = 1 + sum(int(bit) * 2**(-i-1) for i, bit in enumerate(mantissa))
    
    print(f"Sign: {sign_value}")
    print(f"Exponent: {exponent_value}")
    print(f"Mantissa: {mantissa_value}")
    print(f"Actual value: {sign_value} * 2^{exponent_value} * {mantissa_value}")

print_float_representation(0.123)
