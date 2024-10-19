import os
import socket
from collections import Counter
import re

def word_count(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read().lower()
        content = re.sub(r"[^\w\s']", '', content)
        words = content.split()
        return words

def count_words_and_top(filepath):
    words = word_count(filepath)
    total_words = len(words)
    word_freq = Counter(words)
    top_3 = word_freq.most_common(3)
    return total_words, top_3

# Part A & C
total_words_if, top_3_if = count_words_and_top('/home/data/IF.txt')

# Part B
def handle_contractions(text):
    # Replace common contractions with their expanded forms
    text = re.sub(r"(?i)\b(can't)\b", "cannot", text)
    text = re.sub(r"(?i)\b(won't)\b", "will not", text)
    text = re.sub(r"(?i)\b(\w+)'ll\b", r"\1 will", text)
    text = re.sub(r"(?i)\b(\w+)'re\b", r"\1 are", text)
    text = re.sub(r"(?i)\b(\w+)'ve\b", r"\1 have", text)
    text = re.sub(r"(?i)\b(\w+)'t\b", r"\1 not", text)  # This fixes "don't" -> "do not"
    text = re.sub(r"(?i)\b(\w+)'s\b", r"\1 is", text)
    text = re.sub(r"(?i)\b(\w+)'d\b", r"\1 would", text)
    return text


# Pard D
words = handle_contractions(' '.join(word_count('/home/data/AlwaysRememberUsThisWay.txt')))
total_words = len(words.split())
word_freq = Counter(words.split())
top_3 = word_freq.most_common(3)

# Part E
ip_address = socket.gethostbyname(socket.gethostname())

# Part F
output_path = "/home/data/output/result.txt"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, 'w') as f:
    f.write(f"Total words in IF.txt: {total_words_if}\n")
    f.write(f"Top 3 words in IF.txt: {top_3_if}\n")
    f.write(f"Total words in AlwaysRememberUsThisWay.txt: {total_words}\n")
    f.write(f"Top 3 words in AlwaysRememberUsThisWay.txt: {top_3}\n")
    f.write(f"Container IP Address: {ip_address}\n")

# Print result to console
with open(output_path, 'r') as f:
    print(f.read())
