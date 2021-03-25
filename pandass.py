import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv('train.csv')
# print(df[df["Survived"] == 1 ][df['Sex']== 'male'])
# dic = {'col1': range(10), 'col2': range(10)}
# df = pd.DataFrame(dic)
#df.index = ["a","b","c","a","b","c","a","b",5,7]
#df.drop(range(10),0,inplace=True)=
# print(df.describe())
#df["Survived"] = True if  df["Survived"]== 1  else False
def f (x) :
    return x+1000
# df['Age'].apply(func=f)
#df['Age','Sex'].plot(kind="bar")
plt.show()
#df.to_csv('iskander.csv')
print(df['Age'])