from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk
import re
import pandas as pd

nltk.download('stopwords')

df = pd.read_csv("chatbot_coping_posts.csv")

text_blob = ' '.join(df['text'].dropna().values).lower()
text_blob = re.sub(r'[^\w\s]', '', text_blob)
stop_words = set(stopwords.words('english'))
custom_stopwords = stop_words.union({
    'im', 'dont', 'didnt', 'youre', 'got', 'chatgpt', 'replika', 'user', 'ai',
    'know', 'thing', 'one', 'like', 'get', 'would', 'also', 'use', 'make'
})

filtered_words = [word for word in text_blob.split() if word not in custom_stopwords]

wc = WordCloud(width=800, height=400, background_color='white').generate(' '.join(filtered_words))

plt.figure(figsize=(12, 6))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title("Filtered Word Cloud: Chatbot Coping Themes")
plt.tight_layout()
plt.savefig("wordcloud_chatbot_coping_filtered.png")
plt.show()
