tabby_cat = "\tI'm tabbed in"
persian_cat="I'm split\non a line"
backslash_cat="I'm \\a \\cat"

fat_cat="""
I'll do a list:
\t*cat
\t*fish
"""

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
# print the content in fat_cat
print ("%r" % fat_cat)
# print the content that fat_cat is interpreted
print ("%s" % fat_cat)
