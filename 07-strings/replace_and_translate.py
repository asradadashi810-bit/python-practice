# replace and translate on strings

# replace with a limited count
A = "abc xyz abc xyz abc xyz abc xyz"
A = A.replace("b", "Q", 3)   # the first three b's become Q
A = A.replace("Q", "b", 1)   # only the first Q is changed back
print(A)

# Simple encoding with maketrans / translate
fullname = "iau"

encode = str.maketrans("aeiourm", "ZLMSPNW")
decode = str.maketrans("ZLMSPNW", "aeiourm")

encoded = fullname.translate(encode)
decoded = encoded.translate(decode)   # decoding must be done on the encoded text

print(encoded)   # MZP
print(decoded)   # iau
