import re,csv
f = open('C:/Users/sachi/OneDrive/Desktop/Task/Main_Directory/onelinefile.txt','r')
for i in f:
        n = re.findall(r'[+-]?[0-9]+\.[0-9]+', i)
        a = re.findall(r'[a-zA-Z]+', i)
        j = 0
        for p in range(len(n)):
            with open('Filename2.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([str(p+1), a[j],n[p],a[j+1]])
            j += 2

with open('Filename2.csv', 'r',) as file:
    reader = csv.reader(file)
    for row in reader:
        print(','.join(row))