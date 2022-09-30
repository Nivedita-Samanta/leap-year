#to check if it is a leap year
a=int(input())
if (a%400==0) or (a%100!=0) and(a%4==0):
  print("Yes it is a leap year")
else:
  print("No it is not a leap year")
print("THANK YOU")
