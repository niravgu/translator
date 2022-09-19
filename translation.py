from textblob import TextBlob
bl = TextBlob ("comment vas-tu?")
#detect
print (bl.detect_language())
#translate
print (bl.translate (to = 'en'))
print (bl.translate(to = 'hi'))
print (bl.translate(to = 'zh'))
print (bl.translate (to = 'ja'))
