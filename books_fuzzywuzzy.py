# -*- coding: utf-8 -*-
"""
NLP example using book ratings data from Kaggle
"""

# =============================================================================
#  import libraries
# =============================================================================
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


# =============================================================================
#  import book data
# =============================================================================

df = pd.read_csv('books.csv', encoding='latin-1')

# =============================================================================
#  input queries ("querys") in list form below 
# =============================================================================

querys = ['the lion', 'the witch', 'the wardrobe']

# =============================================================================
# execute code
# =============================================================================
# number of "querys"
n = len(querys)

# dataframe with calculated score
dfout = pd.DataFrame(process.extract(querys[0],df['title'], 
                scorer=fuzz.token_set_ratio), columns=('title', 'ratio', 'ind'))


# if there is more than one query, repeat
if n >1:
    for q in range(1, n):
        df3 = pd.DataFrame(process.extract(querys[q],df['title'],
               scorer=fuzz.token_sort_ratio), columns=('title', 'ratio', 'ind'))
        dfout =dfout.append(df3)
# drop duplicates
dfout.drop_duplicates(subset ="title", 
                     keep = False, inplace = True)
# sorting by ratio value 
dfout.sort_values("ratio", inplace = True, ascending=False) 
# reset index
dfout =dfout.reset_index(drop=True)
