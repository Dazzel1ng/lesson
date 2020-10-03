import re

mytest = "Vasya aaaaaaaaaaa 1256, Oleg 1256, aaaaaaaa@gmail.com," \
         "Hasya aaaazaaaaaa 1256, ruseg 1256, aaa@gmail.com," \
         "Sasya aaaaaaaaaaa 1266, Oleg 1256,2003,dead@gmail.com," \
         "Dasya aaaaaaaAZaaa 1256, Oleg 1256, aaaaaaaa@gmail.com," \
         "Gasya aaaaaaaAaaa 1256, Oleg 1256, fast@gmail.com,"



"""
\d = Any Digit 0-9
\D = Any non DIGIT 
\w = Any Alpshabet symbol [A-Z a-z]
\w = Any non Alphabet symbol
\s = breakspace
\S = non breakspace 

[0-9]{3}
[A-Z][a-z]+
\w

"""





textlookfor =r"@\w+\.\w+"
allresults = re.findall(textlookfor,mytest)

print(allresults)



