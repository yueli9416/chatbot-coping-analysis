import pandas as pd

df = pd.read_csv("chatbot_coping_posts.csv")
themes = {
    "emotional_support": ["support", "talk", "feel better", "vent", "relief"],
    "distraction": ["distraction", "pass time", "bored", "scrolling", "escape"],
    "loneliness": ["lonely", "alone", "companionship", "connect"],
    "stress_anxiety": ["stress", "anxiety", "panic", "overwhelmed", "cope"],
    "mental_health": ["depressed", "therapy", "mental health", "sad"]
}

def label_theme(text):
    text = text.lower()
    found_themes = []
    for theme, keywords in themes.items():
        if any(kw in text for kw in keywords):
            found_themes.append(theme)
    return ', '.join(found_themes) if found_themes else 'none'

df['themes'] = df['text'].apply(label_theme)
df.to_csv("chatbot_coping_posts_tagged.csv", index=False)

print(df['themes'].value_counts())
