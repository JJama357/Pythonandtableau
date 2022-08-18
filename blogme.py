# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 17:16:52 2022

@author: Jam
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#reading excel or xlsx files
data= pd.read_excel('articles.xlsx')

#summary of the data
data.describe()
#summary of the columns
data.info()

#counting th number of articles per source
#format of the groupby: df.groupby(['column_to_group'])('column_to_count').count()
data.groupby(['source_id'])['article_id'].count()

#number of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()
data=data.drop('engagement_comment_plugin_count', axis=1)

def thisfunction():
    print('This is my first function')
   
thisfunction()

#This ia function with variables

def aboutme(name, surname,location):
    print('This is ' + name + ' my surname is ' + surname+' I am from ' + location)

a= aboutme('Jamin','Jama','USA')

#using for loops in functions
def favfood(food):
    for x in food:
        print('Top food is ' + x)
fastfood=['salad', 'water', 'fruit']
favfood(fastfood)

#creating a keyword flag
keyword='crash'

#creating a for loop to isolate each title row

# length=len(data)
# keyword_flag=[]
# for x in range(0,length):
#     heading=data['title'][x]
#     if keyword in heading:
#         flag=1
#     else:
#         flag=0
#         keyword_flag.append(flag)

#creating a funtion
def keywordflag(keyword):
    length=len(data)
    keyword_flag=[]
    for x in range(0,length):
        heading=data['title'][x]
        try:
            if keyword in heading:
                flag=1
            else:
                flag=0
        except:
            flag=0
        keyword_flag.append(flag)
    return keyword_flag
    
keywordflag=keywordflag('murder')

#creating a new column in data frame
data['keyword_flag']= pd.Series(keywordflag)

#SentimentIntensityAnalyzer

sent_int= SentimentIntensityAnalyzer()

text=data['title'][16]
sent= sent_int.polarity_scores(text)

neg=sent['neg']
pos=sent['pos']
neu=sent['neu']

#adding a for loop to extract sentiment per title

title_neg_sentiment=[]
title_pos_sentiment=[]
title_neu_sentiment=[]
length=len(data)
for x in range(0,length):
    try:
        text=data['title'][x]
        sent_int= SentimentIntensityAnalyzer()
        sent= sent_int.polarity_scores(text)
        neg=sent['neg']
        pos=sent['pos']
        neu=sent['neu']
    except:
        neg=0
        pos=0
        neu=0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment=pd.Series(title_neg_sentiment)
title_pos_sentiment=pd.Series(title_pos_sentiment)
title_neu_sentiment=pd.Series(title_neu_sentiment)

data['title_neg_sentiment']=title_neg_sentiment
data['title_pos_sentiment']=title_pos_sentiment
data['title_neu_sentiment']=title_neu_sentiment

#writing the data

data.to_excel('blogme_clean.xlsx',sheet_name='blogmedata',index= False)