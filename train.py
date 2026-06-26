import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from preprocess import clean_text

# Load both datasets
fake = pd.read_csv('data/Fake.csv')
real = pd.read_csv('data/True.csv')

# Add labels
fake['label'] = 0  # 0 = Fake
real['label'] = 1  # 1 = Real

# Combine both
df = pd.concat([fake, real], ignore_index=True)

print("Dataset shape:", df.shape)
print("Label distribution:\n", df['label'].value_counts())

# Combine title and text
df['content'] = df['title'].fillna('') + ' ' + df['text'].fillna('')

# Clean text
print("\nCleaning text...")
df['content'] = df['content'].apply(clean_text)

# Features and labels
X = df['content']
y = df['label']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# TF-IDF Vectorization
print("Vectorizing...")
tfidf = TfidfVectorizer(max_features=5000)
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Train model
print("Training model...")
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

# Evaluate
y_pred = model.predict(X_test_tfidf)
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save model and vectorizer
joblib.dump(model, 'model/model.pkl')
joblib.dump(tfidf, 'model/tfidf.pkl')
print("\nModel saved successfully!")