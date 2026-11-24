# Sentiment Analysis using NLP

from textblob import TextBlob

text = input("Enter a sentence: ")

analysis = TextBlob(text)
score = analysis.sentiment.polarity

print("Sentiment Score:", score)

if score > 0:
    print("Positive Sentiment")
elif score < 0:
    print("Negative Sentiment")
else:
    print("Neutral Sentiment")
