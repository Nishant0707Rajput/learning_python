a_string = "this is a \n split and \t\t tabbed string"
print(a_string)

raw_string = r"this is a \n split and \t\t tabbed string"
print(raw_string)

b_string = "this is a " + chr(10) +" split and " + chr(9) + chr(9) + " tabbed string"
print(b_string)

backslash_string = "this is a backslash \followed by string"
print(backslash_string)

backslash_string = "this is a backslash \\followed by string"
print(backslash_string)

error_string = "there is a backslash at the end \\"  #------>single \ not allowed at the end in raw_string
print(error_string)