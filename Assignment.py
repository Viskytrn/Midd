#A program to check whether a year is a leap year or not

year=2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010
for year in range(2000,2010):
    if year % 4==0:
        print(year,"Is a leap year")
    else:
        print(year,"Is not a leap year")

#A program to check whether a letter is a consonant or a vowel


letters="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
letters_list=letters.split(",") #Converts the string into a list
vowels="a,e,i,o,u"
for letters in letters_list:
    if letters in vowels:
        print(letters,"is a vowel")
    else:
        print(letters,"is a consonant")