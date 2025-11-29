# Text Analyzer - Word & Character Counting

def analyze_text(text):
    words = len(text.split())
    characters = len(text.replace(" ", ""))

    print("Total Words:", words)
    print("Total Characters:", characters)

# Example:
sample = "Welcome to Python Internship Week 3"
analyze_text(sample)
