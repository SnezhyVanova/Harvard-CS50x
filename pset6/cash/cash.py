n = 0
while True:
    change = float(input("Type your change: "))
    if int(change) == 0:
        break
    elif change > 0:
        break

r = round(change * 100)
while (r-1) >= 0:
   if (r-25) >= 0:
      r = r-25
      n+=1
   elif (r-10) >= 0:
      r=r-10
      n+=1
   elif (r-5) >= 0:
      r=r-5
      n+=1
   else:
      r=r-1
      n+=1
print (n)