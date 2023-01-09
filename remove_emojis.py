import regex as re


with open("emoji_pattern.txt", "rb") as file:
    emojis = file.read().decode("utf-8")

emoji_pattern = re.compile(emojis, flags=re.UNICODE)

text = "فرحتي أن خنيدة سوت لايك بالغلط من قوة عاطفتها للمعارضة😭  إلى أين يا خنيدة💔😭  عقدة النقص💔"

# remove emojies
clean_text = emoji_pattern.sub(r'', text)

print("Original text: ", text)
print("Cleaned text: ", clean_text)

