txt = 'ABC abc'
b = bytearray(txt, 'ASCII')
len(txt)
len(b)

for i in range(len(b)):
    print(b[i])

# 1. Which byte-values do the 7 different symbols correspond to (ABCabc and space)?
a_values = [ord(char) for char in txt if ord(char) < 128]
print("\nASCII Values: ", a_values)

# 2. Try to convert 'ÅÄÖ' to an ASCII-byte-array
svenska = 'ÅÄÖ'
try:
    sveToASCII = [ord(char) for char in svenska if ord(char) < 128]
    print("\nASCII VALUES: ", sveToASCII)

except:
    print("error: {exception}")

# 3. 