# importing modules
from textblob import TextBlob
#creating a variable holding a sentence
x = TextBlob(input ("please type a sentence"))
#coreecting it
x = x.correct()

print (x)