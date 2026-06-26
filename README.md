# Fake News Detection System

A machine learning web application that detects whether a news article is real or fake using Natural Language Processing (NLP) and Logistic Regression classification.

---

## Project Overview

This project is an AI-powered fake news detection system built using Python, Flask, and Scikit-learn. Users can paste any news article or headline into the web interface and receive an instant prediction with a confidence score indicating whether the content is real or fake.

---

## Features

- Real-time fake news classification using machine learning
- Confidence score displayed with every prediction
- Clean and responsive web interface
- Text preprocessing using NLP techniques
- TF-IDF vectorization for feature extraction
- Sample article loader for quick testing
- Trusted news source links for manual verification
- Word and character count display
- Analysis breakdown showing model details

---

## Tech Stack

| Technology     | Purpose                                      |
|----------------|----------------------------------------------|
| Python 3.x     | Core programming language                    |
| Flask          | Web framework for backend and routing        |
| Scikit-learn   | Machine learning model training              |
| NLTK           | Natural language processing and text cleaning|
| Pandas         | Data loading and manipulation                |
| NumPy          | Numerical computations                       |
| TF-IDF         | Text vectorization (5000 features)           |
| Joblib         | Model serialization and loading              |
| HTML/CSS       | Frontend interface                           |
| Font Awesome   | Icons used in the UI                         |

---

## Project Structure

```
AI_FAKE_NEWS_DETECTION/
├── data/
│   ├── Fake.csv               # Fake news dataset
│   └── True.csv               # Real news dataset
├── model/
│   ├── model.pkl              # Trained Logistic Regression model
│   └── tfidf.pkl              # Fitted TF-IDF vectorizer
├── templates/
│   └── index.html             # Main HTML web page
├── static/
│   └── style.css              # CSS styling for the UI
├── preprocess.py              # Text cleaning and preprocessing
├── train.py                   # Model training script
├── create_dataset.py          # Script to generate sample dataset
├── app.py                     # Flask web application
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## Installation and Setup

### Prerequisites

- Python 3.8 or above
- pip package manager
- Virtual environment (recommended)

### Step 1 - Clone or create the project folder

```bash
mkdir AI_FAKE_NEWS_DETECTION
cd AI_FAKE_NEWS_DETECTION
```

### Step 2 - Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac or Linux
```

### Step 3 - Install dependencies

```bash
pip install flask scikit-learn pandas numpy nltk joblib
```

### Step 4 - Prepare the dataset

Download the Fake and Real News Dataset from Kaggle:
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

Place the downloaded Fake.csv and True.csv files inside the data/ folder.

Alternatively, run the sample dataset generator for testing:

```bash
python create_dataset.py
```

### Step 5 - Train the model

```bash
python train.py
```

This will preprocess the data, train the Logistic Regression model, evaluate it, and save the model files inside the model/ folder.

### Step 6 - Run the web application

```bash
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## How It Works

1. The user pastes a news article or headline into the text box.
2. The text is cleaned using NLP techniques including lowercasing, removing URLs, punctuation, numbers, and stopwords, followed by stemming.
3. The cleaned text is converted into a numerical vector using TF-IDF vectorization with a maximum of 5000 features.
4. The trained Logistic Regression model classifies the vector as real or fake.
5. The result is displayed along with a confidence score percentage.

---

## Model Performance

| Metric         | Value                          |
|----------------|-------------------------------|
| Algorithm      | Logistic Regression            |
| Vectorizer     | TF-IDF (max 5000 features)     |
| Test Split     | 80% train, 20% test            |
| Accuracy       | Up to 95% with full dataset    |

Note: Accuracy with the sample dataset of 30 articles will be lower. For best results, use the full Kaggle dataset with 40,000+ articles.

---

## Usage

1. Open the application in your browser at http://127.0.0.1:5000
2. Paste any news article or headline into the input box
3. Click the Analyze Now button
4. View the prediction result and confidence score
5. Use the trusted source links to manually verify the article

---

## Dataset

The model is trained on the Fake and Real News Dataset available on Kaggle, created by Clement Bisaillon. The dataset contains over 40,000 news articles split into two categories: fake news and real news.

Source: https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

---

## Limitations

- The model is trained on English news articles only.
- Accuracy depends on the size and quality of training data.
- The system is intended for educational purposes and should not be used as the sole method for fact-checking.
- Always verify suspicious news with established fact-checking organizations such as Snopes, Reuters Fact Check, or AP Fact Check.

---

## Trusted Fact-Checking Sources

- BBC News: https://www.bbc.com/news
- Reuters: https://www.reuters.com
- AP News: https://apnews.com
- Snopes: https://www.snopes.com

---

## Future Improvements

- Integrate a larger and more diverse dataset for higher accuracy
- Add support for multiple languages
- Implement deep learning models such as BERT or LSTM for better performance
- Add a URL input option to analyze articles directly from a link
- Deploy the application to a cloud platform such as Render or Heroku
- Add a history section to track previously analyzed articles

---

## Disclaimer

This tool is built for educational purposes as part of a machine learning project. The predictions made by the model are not guaranteed to be accurate. Always cross-check information with trusted and verified news sources before forming conclusions or sharing content.

---

## Author
Mannuru Mahesh
Lovely Professional University 

Project: Fake News Detection System
Technologies: Python, Flask, Scikit-learn, NLTK, TF-IDF, HTML, CSS
