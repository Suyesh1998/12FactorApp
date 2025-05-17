from app.sentiment import analyze_sentiment

def test_positive_sentiment():
    assert analyze_sentiment("I love this!") == "Positive"

def test_negative_sentiment():
    assert analyze_sentiment("I hate this!") == "Negative"

def test_neutral_sentiment():
    assert analyze_sentiment("This is a pen.") == "Neutral"
