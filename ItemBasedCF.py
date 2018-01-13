#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 12:10:23 2018

@author: blaze
"""

import pandas as pd

r_cols=['user_id','movie_id','rating']
ratings=pd.read_csv('u.data',sep='\t',names=r_cols,  usecols=range(3), encoding="ISO-8859-1")

m_cols=['movie_id','title']
movies=pd.read_csv('u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings=pd.merge(movies,ratings)
ratings.head()

userRatings=ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
userRatings.head()

corrMatrix=userRatings.corr()
corrMatrix.head()

corrMatrix=userRatings.corr(method="pearson", min_periods=100)
corrMatrix.head()

myRatings=userRatings.loc[0].dropna()
myRatings

simCandidates=pd.Series()
for i in range(0,len(myRatings.index)):
    sims=corrMatrix[myRatings.index[i]].dropna()
    sims=sims.map(lambda x: x*myRatings[i])
    simCandidates=simCandidates.append(sims)
simCandidates.sort_values(inplace=True, ascending=False)
simCandidates=simCandidates.groupby(simCandidates.index).sum()
simCandidates.sort_values(inplace=True, ascending=False)
simCandidates.head(10)

filteredSims=simCandidates.drop(myRatings.index)
filteredSims.head(10)