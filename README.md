# Sentiment_Score
In this task, we initially accept text input as a paragraph from the user and return the sentiment score of each line in the paragraph.


**app.py** is the python code which makes use of flask in order to create a webapp for the sentiment score prediction.
Initially it renders the **index.html** file which contains having 2 fields and 2 buttons,
Book you read : Text field
Please provide your favourite paragraph: Text field
Submit and Reset Buttons.

After clicking the submit button,the paragraph is segmented into sentences and the sentiment score of each sentence is returned to the user in the form of a table containing two columns namely,Sentence and Sentence Score.

In order to segment the  praragraph into individual sentences,we used **sent_tokenize** method from the **nltk** module.
Similarly in order to obtain the sentiment score as positive, negative, compound/neutral we made use of **SentimentIntensityAnalyzer** from the **nltk.sentiment.vader module**.

