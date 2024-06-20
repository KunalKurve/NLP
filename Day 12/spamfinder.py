from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

from flask import Flask, render_template, request
app = Flask(__name__)

ps = PorterStemmer()
swords = set(stopwords.words('english'))

def clean_txt(sent):
    tokens1 = word_tokenize(sent)  # Step-1. Tokenize the text
    tokens2 = [token for token in tokens1 if token.isalnum()]  # Step-2 Remove the punctuations
    tokens3 = [token for token in tokens2 if token.lower() not in swords]  # Step-3 Remove stopwords
    tokens4 = [ps.stem(token) for token in tokens3]  # step-4 Remove the suffixes
    return tokens4 

classifier = joblib.load("/home/pgdai/Desktop/March24-DAI-Workspace/NLP and CV-June24/Day 12/classifier.model")
tfidf = joblib.load('/home/pgdai/Desktop/March24-DAI-Workspace/NLP and CV-June24/Day 12/preprocessor.model')

@app.route('/')
def text():
    return render_template('spamdetecter.html')

@app.route('/spamfinder', methods=['GET','POST'])
def result():
    if request.method == 'POST':
        data = dict(request.form)
        message = tfidf.transform([data['message']])
        data['result'] = classifier.predict(message)[0]
        return render_template('spamoutput.html', result = data['result'])

if __name__ == '__main__':
    app.run(debug=True)