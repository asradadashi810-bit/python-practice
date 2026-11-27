"""Translate an English .srt subtitle file to Persian.

Only the subtitle text is translated; numbers and timestamps stay untouched.
Needs: pip install deep-translator
"""

from deep_translator import GoogleTranslator

INPUT_FILE = "english.srt"
OUTPUT_FILE = "translated.srt"

translator = GoogleTranslator(source="en", target="fa")

with open(INPUT_FILE, "r", encoding="utf-8") as file:
    text = file.read().replace("\r\n", "\n")

blocks = text.strip().split("\n\n")
result = []

for block in blocks:
    lines = block.split("\n")
    if len(lines) < 3:
        result.append(block)
        continue
    index, timing = lines[0], lines[1]
    content = " ".join(lines[2:])
    translated = translator.translate(content)
    result.append(f"{index}\n{timing}\n{translated}")

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write("\n\n".join(result) + "\n")

print("completed!")
