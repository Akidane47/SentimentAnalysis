
from textblob import TextBlob
from newspaper import Article


url = 'https://www.ycombinator.com/companies/permitflow/jobs/v1HlvWY-permit-operations-lead'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)
