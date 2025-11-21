import json
import re

# Load knowledge base and keyword mapping
with open("heart_guide_sections_fixed.json", "r", encoding="utf-8") as f:
    SECTIONS = json.load(f)

with open("section_keywords.json", "r", encoding="utf-8") as f:
    SECTION_KEYWORDS = json.load(f)

EMERGENCY_KEYWORDS = [
    "chest pain", "shortness of breath", "difficulty breathing", "severe",
    "stroke", "emergency", "911", "unconscious", "fainting", "heart attack"
]
STOPWORDS = {
    'the', 'and', 'for', 'that', 'with', 'you', 'your', 'from', 'this', 'are', 'not',
    'can', 'have', 'has', 'will', 'was', 'all', 'but', 'who', 'get', 'may', 'about',
    'what', 'when', 'how', 'any', 'they', 'their', 'should', 'use', 'doctor', 'more', 'most',
    'is', 'a', 'of', 'to', 'in', 'on', 'as', 'it', 'be', 'if', 'at', 'by', 'we', 'do', 'me', 'my', 'i'
}


def filter_fluff(question):
    # Lowercase and split on word boundaries
    words = re.findall(r'\b\w+\b', question.lower())
    # Filter out stopwords
    filtered = [w for w in words if w not in STOPWORDS]
    return filtered


def is_emergency(question):
    q = question.lower()
    return any(kw in q for kw in EMERGENCY_KEYWORDS)



def ranked_sections(question, top_n=5):
    important_words = set(filter_fluff(question))
    scored = []

    for section, content_keywords in SECTION_KEYWORDS.items():
        # Get the words directly from the section title string
        title_words = set(filter_fluff(section))

        # Score title matches with a higher weight (e.g., 3 points)
        title_score = sum(word in important_words for word in title_words) * 3

        # Score content matches with the base weight (1 point)
        content_score = sum(word in important_words for word in content_keywords)
        
        total_score = title_score + content_score

        if total_score > 0:
            scored.append((total_score, section))

    # Sort total score
    scored.sort(reverse=True)
    return [section for score, section in scored[:top_n]]


def ai_assistant():
    print("Welcome to the Heart Recovery Q&A Assistant!")
    print("Ask your question, or type 'quit' to exit.\n")

while True:
    question = input("Ask your question: ").strip()
    if question.lower() in ("quit", "exit"):
        print("Thank you for using the assistant. Stay healthy!")
        break

    if is_emergency(question):
        print("\n⚠️ This may be an emergency! Please call 911 or your doctor immediately.\n")
      

    section_list = ranked_sections(question, top_n=6)
    if not section_list:
        print("\nSorry, I couldn't find an answer. Please consult your recovery booklet or doctor.")
        print("\nDISCLAIMER: This is general information, not medical advice. Always consult your healthcare provider.\n")
        continue

    shown = set()
    for section in section_list:
        if section not in SECTIONS or section in shown:
            continue
        print(f"\n[Section: {section}]\n")
        print(SECTIONS[section][:2000])
        shown.add(section)
        resp = input("\nWas this helpful? (yes/no): ").strip().lower()
        if resp in ("yes", "y"):
            print("\nGlad I could help! If you have another question, just ask.")
            break
        elif resp in ("no", "n"):
            continue
        else:
            print("I'll take that as a no. Let's keep looking.")
    else:
        print("\nSorry, I've shown all the most likely sections. Please check your booklet or consult your healthcare provider.")

    print("\nDISCLAIMER: This is general information, not medical advice. Always consult your healthcare provider.\n")

   
if __name__ == "__main__":
    ai_assistant()
