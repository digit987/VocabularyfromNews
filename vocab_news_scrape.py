# File words_repo.json taken from https://github.com/dwyl/english-words/words_dictionary.json
# File dictionary.son taken from https://raw.githubusercontent.com/adambom/dictionary/master/dictionary.json
# coding: utf-8

# In[5]:

from newspaper import Article


# In[6]:

article = Article(url="https://www.thehindu.com/news/national/andhra-pradesh/centre-to-soon-take-up-linking-of-godavari-and-cauvery-gadkari/article26051017.ece", language='en')


# In[9]:

article.download()


# In[11]:

article.parse()


# In[13]:

article.nlp()


# In[14]:

print(article.title)


# In[15]:

print(article.text)


# In[16]:

print(article.summary)


# In[17]:

print(article.authors)


# In[18]:

print(article.keywords)


# In[19]:

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))


# In[20]:

from nltk.tokenize import word_tokenize 
tokenized_article = word_tokenize(article.text)


# In[32]:

filtered_words = [word for word in tokenized_article if word.lower() not in stop_words and word != ('' or "" or ',' or '.')]


# In[33]:

print(filtered_words)


# In[58]:

with open('dictionary.json') as dictionary:
    dictionary = json.load(dictionary)


# In[80]:

vocab = {}


# In[82]:

for word in filtered_words:
    if word.upper() in dictionary:
        vocab[word] = dictionary[word.upper()]


# In[83]:

print(vocab)
