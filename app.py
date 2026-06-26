from flask import Flask, render_template, request
import joblib
from preprocess import clean_text

app = Flask(__name__)

model = joblib.load('model/model.pkl')
tfidf = joblib.load('model/tfidf.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    news = request.form['news']
    cleaned = clean_text(news)
    vectorized = tfidf.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    confidence = model.predict_proba(vectorized)[0]

    if prediction == 1:
        result = "REAL NEWS"
        confidence_score = round(confidence[1] * 100, 2)
        color = "green"
    else:
        result = "FAKE NEWS"
        confidence_score = round(confidence[0] * 100, 2)
        color = "red"

    return render_template('index.html',
                           result=result,
                           confidence=confidence_score,
                           color=color,
                           news=news)

if __name__ == '__main__':
    app.run(debug=True)