import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("chatbot_coping_posts_tagged.csv")

from collections import Counter
theme_counts = Counter()

for themes in df['themes']:
    for t in [t.strip() for t in themes.split(',')]:
        if t != 'none':
            theme_counts[t] += 1

theme_df = pd.DataFrame.from_dict(theme_counts, orient='index', columns=['count']).sort_values(by='count', ascending=True)

theme_df.plot(kind='barh', figsize=(8, 6), legend=False)
plt.title("Coping Themes in Chatbot Posts")
plt.xlabel("Number of Posts")
plt.ylabel("Theme")
plt.tight_layout()
plt.savefig("coping_theme_barplot.png")
plt.show()
