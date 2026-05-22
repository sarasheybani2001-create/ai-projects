from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

print("AI is running...")

while True:
    user_input = input("Enter text (or type exit): ")

    if user_input.lower() == "exit":
        break

    result = analyze_sentiment(user_input)
    print("Result:", result)