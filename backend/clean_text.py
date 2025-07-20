
import re
import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))


def basic_clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_text_with_stopwords(text):
    text = basic_clean_text(text)
    words = text.split()
    filtered = [word for word in words if word not in stop_words]
    return ' '.join(filtered)
