Natural language processing (NLP) is a every eolving branch of computer science,
that deals with thhe natural language. Some common examples are "chat bots" thhat can respond
to a typed query. In NLP, text is broken up into tokens, these tokens represent some meaningful 
subset of the mmain text. THESE TOKENS are used together with other tokens to make sense of a natural language text.

In this very short example, we will use a string matching algorithm. In particular, the "fuzzywuzzy" Python library.
Esentially, this package measures distance ( Levenshtein Distance) between strings and calculates a similarity score.

In this example, we will use the Kaggle data set (https://www.kaggle.com/jealousleopard/goodreadsbooks)
of the books in the good reads list. Downloaded on 02/12/2019.

Scenario:

We want to search for a book but we cannont quite remember the name of it. Therefore, we
have several guesses of the book title and run the algorithm to find siimilar matches. The 
guesses are 'the lion', 'the witch', 'the wardrobe'.

The results after running the algorithm are contained in results.csv.