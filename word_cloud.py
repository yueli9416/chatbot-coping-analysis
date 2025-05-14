from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("chatbot_coping_posts.csv")

text_blob = ' '.join(df['text'].dropna().values).lower()
wc = WordCloud(width=800, height=400, background_color='white').generate(text_blob)

plt.figure(figsize=(12, 6))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title("Most Frequent Words in Posts About Chatbot Coping")
plt.tight_layout()
plt.savefig("wordcloud_chatbot_coping.png")
plt.show()
