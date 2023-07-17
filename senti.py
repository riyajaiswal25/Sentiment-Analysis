import nltk
nltk.download('all')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_sentiment(text):
  scores = SentimentIntensityAnalyzer().polarity_scores(text)
  sentiment = 1 if scores['pos']>0 else 0
  return sentiment