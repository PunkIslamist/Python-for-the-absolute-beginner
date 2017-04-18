#get number value
#display "tip values" of 15% and 20%

print("Harro, please tell me a fictional bill amount:")
base = float(input())

tip_15 = base*0.15
tip_20 = base*0.20
tip_total_15 = base+tip_15
tip_total_20 = base+tip_20

print()
print("Ok, so 15% of", base, "is", tip_15, "and 20% would be", tip_20,".")
print("Therefor I recommend that you pay between", tip_total_15, "and",\
      tip_total_20, "in total!")

