import json
import re
from collections import Counter

# Load section titles and their content from JSON file
with open("CSC510-Foundations of Artificial Intelligence/Final Project/heart_guide_sections_fixed.json", "r", encoding="utf-8") as f:
    sections = json.load(f)

# Extract lowercase words of at least 3 letters
def clean_words(text):
    return re.findall(r'\b[a-z]{3,}\b', text.lower())

# Words we want to ignore
STOPWORDS = set([
    'the', 'and', 'for', 'that', 'with', 'you', 'your', 'from', 'this', 'are', 'not',
    'can', 'have', 'has', 'will', 'was', 'all', 'but', 'who', 'get', 'may', 'about',
    'what', 'when', 'how', 'any', 'they', 'their', 'should', 'use', 'doctor', 'more', 'most', 'what'
])

section_keywords = {}

# For each section, get keywords from title and top common words in content
for section, content in sections.items():
    keywords = set(clean_words(section))
    words = [w for w in clean_words(content) if w not in STOPWORDS]
    common_words = [word for word, count in Counter(words).most_common(9) if count > 1]
    keywords.update(common_words)
    section_keywords[section] = sorted(keywords)

# Save keywords for each section to JSON file
with open("section_keywords.json", "w", encoding="utf-8") as f:
    json.dump(section_keywords, f, indent=2)
