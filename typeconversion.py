#Python allows us to convert data types automatically (implicit)
#or manually using type casting (explicit).

#1️ String → Integer
s = "123"
n = int(s)
print(n + 10)

#2️ String → Float
s = "12.5"
f = float(s)
print(f + 1.5)

#3️ Integer → String
x = 100
s = str(x)
print("Value: " + s)

#4 Boolean Conversion
print(bool(1))      # True
print(bool(0))      # False
print(bool(""))     # False
print(bool("Hi"))   # True
