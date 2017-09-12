formatter = "%r %r %r %r"

print (formatter % (1,2,3,4))
print (formatter % (formatter,formatter,formatter,formatter))

print (formatter % ( "I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight." ))

# if there is a single quote in the string, output will be enclosed in double quotes
# else it will be in single quote
print (formatter % ( "I had this thing.",
"That you could type up right.",
"But it did sing.", # remove the single quote here
"So I said goodnight." ))
