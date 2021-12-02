#count the number of times a depth measurement increases from the previous measurement

upcomingDepths = [199,200,208,210,200,207,240,269,260,263]

count = 0
previous = 0

for depth in upcomingDepths:
  if (previous == 0):
    print("do nothing my name jeff")
  elif (depth > previous):
    count += 1

  previous = depth

print(count)
