## Arithmetic operators ##
# + * / // % **

print(5 + 3)

print("hello" + "world!")

print(5 - 3)
print(5 * 3)
print(5 / 3)
print(5 // 3) # return only the integer part
print(5 % 3) # modulo -> returns the reminder of a division
print(5 ** 3)

### Comparison operators ## 
# > >= < <=  == !=

print(5 > 4) # True
print(5 >= 4) # True
print(5 < 4) # False
print(5 <= 4) # False
print(5 == 4) # False
print(5 != 4) # True

# and, or, not

# and operator
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

# or operator 
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

# not operator
print(not True) # False
print(not False) # True

x = 4
y = 6
print(x > 2 and y < 2) # False
print(x > 2 or y < 2) # True

z = 6
print(not (z > 4)) # False
print(not (z < 4)) # True

## Assignment operators ##
# =  +=  -= *= /=
my_var = 5
# compound Assignment
my_var += 2 # my_var = my_var + 2  -  7
my_var -= 2 # 3
my_var *= 2 # 10
my_var /= 2 # 2.5

