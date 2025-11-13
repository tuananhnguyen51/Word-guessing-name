import os
import json
import random as rd

os.makedirs("user_data", exist_ok=True)
file = "user_data/data.json"

if not os.path.exists(file):
    with open(file,"w", encoding="utf-8") as f:
        json.dump({"record" : None} ,f,indent=4,ensure_ascii=False)

def load_data():
    if not os.path.exists(file):
        return {"record": None}
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data 
    except (json.JSONDecodeError, ValueError):
        # Nếu file bị trống hoặc lỗi -> tạo lại mặc định
        data = {"record": None}
        save_data(data)
        return data
    
def save_data(data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data,f, indent=4, ensure_ascii=False)

def logic_game():
    turn = 0
    data = load_data()
    l_words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
    key_word = rd.choice(l_words)
    result = ['_']* len(key_word)
    while True:
        turn += 1
        print(f"word: {' '.join (result)}")
        while True:
            g_keyword = input("- Guess the word -  ").lower()
            if len(g_keyword) > len(key_word):
                print("The word you guess must have less than or equal to the number of letters of the word you are looking for.")
            else:
                break
        temp_result = result.copy()
        for i,ch in enumerate(key_word):
            if ch in g_keyword:
                temp_result[i] = ch
        if "_" not in temp_result and g_keyword != key_word:
            print("⚠️ This guess revealed all the words, so it was hidden!")
            print("Word:", " ".join(["#"] * len(key_word)))
            continue

        result = temp_result

        if g_keyword == key_word:
            print(f"congratulations you did it in {turn} try")
            if data["record"] is None or turn < data["record"]:
                print("🏆 New record!")
                data["record"] = turn
                save_data(data)
            break
            
def main():
    while True:
        data = load_data()
        record_display = "No record yet" if data["record"] is None else f"{data['record']} try"
        print(f"Welcome to 'Word guessing game' chose an option\n1.Rules\n2.Start\n3.Quit\n=== your record is {record_display}")
        chosen = input()
        if chosen == "1":
                print("""
🎮 Word Guessing Game – Rules

1. Objective
   - Guess the secret word chosen by the game.
   - You can guess one letter at a time or try to guess the whole word.

2. How to Play
   - The word is displayed as _ _ _ _ _ _ (underscores represent hidden letters).
   - Enter a letter or a word for your guess.
   - If your guessed letter is in the secret word, it will be revealed in the correct positions.
   - If you guess the whole word correctly, you win immediately.

3. Special Rules
   - If a guess fills all remaining blanks at once but is not the correct word,
     the game will hide the result for that turn and display # # # # # instead.
     This prevents "lucky guesses" from revealing the word.
   - You can guess as many times as you like until you find the word.

4. Winning the Game
   - The game ends when you either:
     1. Guess the whole word correctly, or
     2. Reveal all letters (without triggering the "hide" rule) — you automatically win.

5. Records
   - The game keeps track of your best record (minimum number of guesses).
   - If you beat your previous record, it will be saved as your new high score.

6. Tips
   - Try to guess letters strategically.
   - Avoid typing long guesses that might fill all blanks unintentionally.
""")
        elif chosen == "2":
            logic_game()
        elif chosen == "3":
            print("Good bye!")
            break
        else:
            pass
main()