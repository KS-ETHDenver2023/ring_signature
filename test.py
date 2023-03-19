def str_to_hex_num(string):
    hex_string = string.encode('utf-8').hex()
    print(hex_string)
    return hex_string
str_to_hex_num("([a,b],[c,d],[e,f]/[x,y]/98998979794)")