#!/usr/bin/env python
# coding: utf-8

# # Visualizing Chipotle's Data

# In[1]:


# Step 1. Import the necessary libraries

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
# set this so the graphs open internally
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called chipo.

chipo=pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv",sep="\t")
chipo["item_price"]=chipo["item_price"].str.replace("$","").astype("float")


# In[3]:


# Step 4. See the first 10 entries
chipo.head(10)


# In[15]:


# Step 5. Create a histogram of the top 5 items bought
top_hist=pd.DataFrame(chipo.value_counts("item_name").iloc[:5]).set_axis(["Qty"],axis=1)
# top_hist.hist()
top_hist["item_name"]=top_hist.index
top_hist.plot(x='item_name',y='Qty',kind='bar')
plt.show()


# In[16]:


# Step 6. Create a scatterplot with the number of items orderered per order price
plt.scatter(chipo["item_price"],chipo["quantity"],alpha=0.8,)


# In[26]:


# Step 7. BONUS: Create a question and a graph to answer your own question
#  Create a sliced piechart for top 4 quantities per order for whole Data skip the first.
# chipo["quantity"].value_counts()
labels=chipo["quantity"].value_counts().index[1:5]
plt.pie(chipo["quantity"].value_counts()[1:5],explode=[0.1,0.2,0.2,0.6],labels=labels,autopct="%0.1f",shadow=1)
plt.show()


# In[ ]:





# # Online Retails Purchase

# In[142]:


# Step 1. Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[28]:


# Step 2. Import the dataset from this address.
# Note :- if you receive a utf-8 decode error, set encoding = 'latin1' in pd.read_csv() .
# Step 3. Assign it to a variable called online_rt
address= pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Online_Retail/Online_Retail.csv",encoding = 'latin1')
address


# In[32]:


# Step 4. Create a histogram with the 10 countries that have the most 'Quantity' ordered except UK
countries=address[address["Country"]!= "United Kingdom"].groupby("Country")["Quantity"].sum()
top_10=countries.sort_values(ascending=False)[:10]
plt.bar(top_10.index,top_10.values)
plt.xlabel('Country')
plt.ylabel('Quantity Ordered')
plt.title('Top 10 Countries by Quantity Ordered (Excluding UK)')
plt.xticks(rotation=90)
plt.show()


# In[122]:


# Step 5. Exclude negative Quantity entries
address = address[address["Quantity"] > 0 ]


# In[45]:


# Step 6. Create a scatterplot with the Quantity per UnitPrice by CustomerID for the top 3 Countries (except UK)
top3_countries = address[address["Country"] != "United Kingdom"].groupby("Country")["Quantity"].sum().nlargest(3).index
data = address[address["Country"].isin(top3_countries)].groupby(["CustomerID","Country"])['Quantity','UnitPrice'].sum().reset_index()
data["QuantityPerPrice"]= data["Quantity"] / data["UnitPrice"]
for country in top3_countries:
    subset = data[data["Country"]==country]
    plt.scatter(subset['CustomerID'], subset['QuantityPerPrice'], label=country)

plt.xlabel('CustomerID')
plt.ylabel('Quantity per UnitPrice')
plt.title('Quantity per UnitPrice by CustomerID for Top 3 Countries (Excluding UK)')
plt.legend()
plt.show()


# In[ ]:


# Step 7. Investigate why the previous results look so uninformative.

# the choice of visualization and the informativeness of the results depend on the nature of your data and the specific insights 
# you're seeking to uncover.Experimenting with different approaches and visualizations can 
# often lead to a more informative representation of the data.


# In[86]:


# 8. Plot a line chart showing revenue (y) per UnitPrice (x).
data = address[(address["Quantity"] > 0) & (address["UnitPrice"] > 0)]
data["Revenue"] = data["Quantity"] * data["UnitPrice"]
line=data.groupby("UnitPrice")["Revenue"].sum().nlargest(5)
plt.plot(line.index,line.values)
plt.show()


# In[147]:


# 8.1 Group UnitPrice by intervals of 1 for prices [0,50), and sum Quantity and Revenue .

ad1=data[(data["UnitPrice"]<=50) & (data["UnitPrice"] > 0)]
ad1['unit_price']=ad1['UnitPrice']//1
ans=ad1.groupby('unit_price')['Quantity','Revenue'].sum()
ans["Revenue"] = (ans["Revenue"] / 1000000).round(5)                 # ".round(Num of Decimal points)"    Most IMP
ans["Quantity"] = (ans["Quantity"]/1000000)


# In[180]:


# 8.3 Plot.
# 8.4 Make it look nicer.
plt.bar(ans.index+0.2,ans["Revenue"],width=0.4,label="Revenue")
plt.bar(ans.index-0.2,ans["Quantity"],width=0.4,label="Quantity")
plt.legend()
plt.show()


# In[ ]:





# # Scores

# In[181]:


# Step 1. Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt


# In[182]:


# Step 2. Create the DataFrame that should look like the one below.
scores = pd.read_csv("Scores.txt",sep=" ")
scores


# In[185]:


# Step 3. Create a Scatterplot of preTestScore and postTestScore, with the size of each point determined by age
plt.scatter(scores["preTestScore"],scores["postTestScore"],s=scores["age"])
plt.xlabel("preTestScore")
plt.ylabel("postTestScore")
plt.show()


# In[196]:


# Step 4. Create a Scatterplot of preTestScore and postTestScore
plt.scatter(scores["preTestScore"],scores["postTestScore"],s=scores["postTestScore"]*4.5,c=scores["female"])
plt.legend()
plt.show()


# In[ ]:





# # Tips

# In[4]:


# Step 1. Import the necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[5]:


# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called tips
tips = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Tips/tips.csv")
tips


# In[6]:


# Step 4. Delete the Unnamed 0 column
tips =tips.drop(columns="Unnamed: 0")


# In[7]:


# Step 5. Plot the total_bill column histogram
plt.hist(tips["total_bill"],alpha=0.8)
plt.show()


# In[8]:


# Step 6. Create a scatter plot presenting the relationship between total_bill and tip
plt.scatter(tips["total_bill"],tips["tip"])
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()


# In[ ]:





# In[9]:


# Step 7. Create one image with the relationship of total_bill, tip and size.
sns.load_dataset("tips")
sns.set(style="whitegrid") #style must be one of white, dark, whitegrid, darkgrid, ticks
sns.pairplot(tips, vars=["total_bill", "tip", "size"])
plt.show()


# In[15]:


# Step 8. Present the relationship between days and total_bill value

sns.boxplot(x=tips["day"],y=tips["total_bill"])
plt.show()


# In[17]:


# Step 9. Create a scatter plot with the day as the y-axis and tip as the x-axis, differ the dots by sex
sns.scatterplot(x=tips["day"],y=tips["tip"],hue=tips["sex"])
plt.show()


# In[21]:


# Step 10. Create a box plot presenting the total_bill per day differetiation the time (Dinner or Lunch)
sns.boxplot(x=tips["day"],y=tips["total_bill"],hue=tips["time"])
plt.show()


# In[20]:


# Step 11. Create two histograms of the tip value based for Dinner and Lunch. They must be side by side.

plt.subplot(1,2,1)
sns.histplot(data=tips[tips['time'] == 'Dinner'], x='tip', bins=15, kde=True, color='skyblue')

plt.subplot(1,2,2)
sns.histplot(data=tips[tips['time'] == 'Lunch'], x='tip', bins=15, kde=True, color='salmon')


# In[32]:


# Step 12. Create two scatterplots graphs, one for Male and another for Female, presenting the total_bill value and tip
#          relationship, differing by smoker or no smoker
plt.subplot(1,2,1)   
sns.scatterplot(x=tips[tips["sex"]=="Male"]["tip"],y=tips[tips["sex"]=="Male"]["total_bill"],hue=tips["smoker"])
plt.title("Male Relationship")

plt.subplot(1,2,2)   
sns.scatterplot(x=tips[tips["sex"]=="Female"]["tip"],y=tips[tips["sex"]=="Female"]["total_bill"],hue=tips["smoker"])
plt.title("Female Relationship")


# In[ ]:





# # Visualizing the Titanic Disaster

# In[34]:


# Step 1. Import the necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[36]:


# Step 2. Import the dataset from this address
# Step 3. Assign it to a variable titanic
titanic=pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Titanic_Desaster/train.csv")
titanic


# In[38]:


# Step 4. Set PassengerId as the index
titanic.set_index("PassengerId",inplace=True)


# In[63]:


# Step 5. Create a pie chart presenting the male/female proportion
plt.pie(titanic["Sex"].value_counts(),autopct='%0.2f',labels=titanic["Sex"].value_counts().index,shadow=1,explode=[0.05,0])
plt.legend()
plt.show()


# In[67]:


# Step 6. Create a scatterplot with the Fare payed and the Age, differ the plot color by gender
sns.scatterplot(x=titanic["Age"],y=titanic["Fare"],hue=titanic["Sex"])
plt.show()


# In[71]:


# Step 7. How many people survived?
print("Survived :",titanic["Survived"].value_counts()[1])


# In[87]:


# Step 8. Create a histogram with the Fare payed
sns.histplot(x=titanic["Fare"].value_counts())
plt.show()


# In[ ]:





# # Pokemon

# In[88]:


# Step 1. Import the necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[92]:


# Step 2. Create a data dictionary that looks like the DataFrame below
# Step 3. Assign it to a variable called pokemon
pokemon=pd.read_csv('pokemon.txt',sep=" ")
pokemon


# In[112]:


# Step 4. Ops...it seems the DataFrame columns are in alphabetical order. Place the order of the columns as name, type, hp, evolution, pokedex
pokemon=pokemon.loc[:,['name','type','hp','evolution','pokedex']]


# In[116]:


# Step 5. Add another column called place, and insert what you have in mind.
pokemon["place"] = ["Russia","Germany","UK","USA"]


# In[118]:


# Step 6. Present the type of each column
pokemon.info()


# In[ ]:





# # Apple Stock
# 

# In[119]:


# Step 1. Import the necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[121]:


# Step 2. Import the dataset from this address
# Step 3. Assign it to a variable apple
apple = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv")
apple


# In[122]:


# Step 4. Check out the type of the columns
apple.info()


# In[126]:


# Step 5. Transform the Date column as a datetime type
apple["Date"]=pd.to_datetime(apple["Date"])
apple["Date"].info()


# In[127]:


# Step 6. Set the date as the index
apple.set_index("Date")


# In[133]:


# Step 7. Is there any duplicate dates?
apple["Date"].value_counts()
# No There is not any Duplicate Date


# In[149]:


# Step 8. Ops...it seems the index is from the most recent date. Make the first entry the oldest date.
apple.sort_values("Date",inplace=True)
apple.set_index("Date",inplace=True)


# In[159]:


# Step 9. Get the last business day of each month
apple.resample('M').last()


# In[176]:


# Step 10. What is the difference in days between the first day and the oldest
first_day=apple.index.min()
oldest_day=apple.index.max()

difference = (oldest_day - first_day).days
difference


# In[178]:


# Step 11. How many months in the data we have?
len(apple.resample("M").last())


# In[192]:


# Step 12. Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches
plt.figure(figsize=[13.5,9])
plt.plot(apple["Adj Close"])
plt.show()

