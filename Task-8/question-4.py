import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])

print("Original Series:")
print(ser)
result = ser.map(lambda x: x[0].upper() + x[1:-1] + x[-1])
for i in result:
    print(i,end=' ')



