from docx import Document
import json

doc_path = "DignityHeartHandOutFull.docx"
doc = Document(doc_path)

sections = {}
current_section = None
current_content = []

def is_heading(para):
    """Detect if paragraph is a heading by style or manual check."""
    # Heading style detection
    if para.style.name.startswith("Heading"):
        return True
    # Large/bold font or ALL CAPS check
    if para.text.isupper() and len(para.text) > 3:
        return True
    return False

# Extract sections
for para in doc.paragraphs:
    text = para.text.strip()
    if not text:
        continue
    if is_heading(para):
        if current_section and current_content:
            sections[current_section] = "\n".join(current_content).strip()
        current_section = text
        current_content = []
    else:
        current_content.append(text)

# Add the last section
if current_section and current_content:
    sections[current_section] = "\n".join(current_content).strip()

# Save to JSON
with open("heart_guide_sections.json", "w", encoding="utf-8") as f:
    json.dump(sections, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(sections)} sections. Saved to heart_guide_sections.json")
