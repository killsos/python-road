from sys import argv

script, fileName = argv

txt = open(fileName)

print "Here's your file %r:" %fileName

print txt.read()

print "Type the fileName again"

file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()