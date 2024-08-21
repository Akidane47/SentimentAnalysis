
from textblob import TextBlob
from newspaper import Article


url = #input your url here
article = Article(url)

#section below downloads, parses, and applies the language processing to the article
article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)
