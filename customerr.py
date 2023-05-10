

import pandas as pd

df=pd.read_csv('C:/Users/vijay/Downloads/Market_Basket_Optimisation.xls')
transactions=[]
for i in range(0,7500):
    transactions.append([str(df.values[i,j]) for j in range(0,20)])
    

from apyori import apriori
rules=apriori(transactions=transactions,min_support=0.003,min_confidence=0.2,min_lift=3,min_length=2,max_length=2)

results=list(rules)

print(results)

base= [str(result.ordered_statistics[0][0]) for result in results]
add=  [str(result.ordered_statistics[0][1]) for result in results]
support=[result.support for result in results]
confidence=[str(result.ordered_statistics[0][2]) for result in results]
lift=[str(result.ordered_statistics[0][3]) for result in results]




li=list(zip(base,add,support,confidence,lift))
df1=pd.DataFrame(li,columns=['base','add','support','confidence','lift'])