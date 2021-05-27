from flask import Flask,render_template,request
from nltk import sent_tokenize
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app=Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/getprediction',methods=['POST'])
def getprediction():
    text=request.form.get('text')
    sentences=sent_tokenize(text)
    sia=SentimentIntensityAnalyzer()
    x=['{}'.format(i) for i in sentences]
    y=['{}'.format(sia.polarity_scores(i)) for i in sentences]
    combined=list(zip(x,y))
    table=pd.DataFrame(combined,columns=['Sentence','Sentiment Score'])
    output_table=table.to_html()

    return output_table

if __name__=='__main__':
    app.run(debug=True)