def caesar(shift_num, string):
    string = string.lower()
    upper = ord('a')
    lower = ord('z')
    new_str = ''
    for c in string:
        cur = ord(c)
        if c in [' ']:
            new_str += c
        elif (cur + shift_num) > lower:
            new_str += chr(upper + (lower-cur + 1))
        elif (cur + shift_num) < upper:
            new_str += chr(lower - (abs(shift_num) - (cur-upper) - 1))
        else:
            new_str += chr(cur+shift_num)
    return new_str

print(caesar(4, 'all'))
print(caesar(-4, caesar(4, 'all')))
print(caesar(-4, caesar(4, 'abandon all hope for death is only the beginning')))
print(caesar(-4, 'Eferhsr epp lsti jsv hiexl mw srpc xli fikmrrmrk'))
