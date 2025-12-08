# quiz_game.py

questions = {
    "What is the capital of India? ": "Delhi",
    "Who developed Python? ": "Guido van Rossum",
    "What is 5 + 7? ": "12"
}

score = 0

for q, a in questions.items():
    ans = input(q)
    if ans.strip().lower() == a.lower():
        score += 1

print(f"Your score: {score}")

# save score
with open("quiz_scores.txt", "a") as f:
    f.write(f"Score: {score}\n")
