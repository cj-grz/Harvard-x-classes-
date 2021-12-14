# getting start with pandas
# SERIES
import pandas as pd
x=pd.Series([6,3,8,6])
x=pd.Series([6,3,8,6],
			index=list("qwer"))
# print(x)
# print(x['w'])

age={"Tim":29, "Jim":31, "Adam":19}
y = pd.Series(age)

# DATAFRAMES
data = {'name': ['Tim', 'Jim', 'Pam','Sam'],
		'age' : [  29 ,  31  ,  27  ,  35 ],
		'ZIP' : ['02115','02130','67700','00100']
		}
x = pd.DataFrame(data, columns=['name', 'age', 'ZIP'],
				 index=list("qwer"))

# DATAFRAMES