zodiac = ["Rat","Ox","Tiger","Hare","Dragon","Snake","Horse","Goat","Monkey","Chicken","Dog","Pig"]

#Validation for year
def main(year):
  while year < 0 or year > 9999:
    year = int(input("Enter a valid year: "))
  

#Defining chinese zodiac according to the year 
def CZ(year):
  index = (year-4)%12
  return zodiac[index]
  
year = int(input("Enter a year: "))
main(year)
CZ(year)
print(f'year {year} is the year of {CZ(year)}')

'''
By : Chang Chung Cheok 
Array : zodiac 
variable : year 
objective : Display chinese zodiac associated with that year
'''
