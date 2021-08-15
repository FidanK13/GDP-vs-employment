import csv
#with
u=open('./unemp.csv') #as r:
cs=csv.reader(u,delimiter=',')
r=open('./gdp.txt')
while True:
    il=input('ili daxil edin')
    if 1948>int(il)>2008:
        print('duzgun il daxil edin')
        continue
    else:
        gdpsum=float(0)
        summa=float(0)

        for i in r:
            if i[0:4]==il:
                gdpsum+=float(i.strip().split(' ')[-1])

        gdpavr=gdpsum/float(4)


        for row in cs:
            if row[0]==il:
                j=row[1:13]
                for i in j:
                    summa+=float(i)
                avr=summa/float(12)
        print(il,' il uchun ortalama ishsizlik : ',avr,' ve ortalama gdp: ' , gdpavr)