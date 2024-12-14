# Quiz game
print(36*"\033[92m=")
print("                Quiz                ")
print(36*"\033[92m=")

questions = ("1. Apa fungsi len()?: ",
            "2. Apa tipe data dari True?: ",
            "3. Apa output dari print(5 % 2)?: ",
            "4. Apa output dari ptint(10 // 3)?: ",
            "5. Apa arti dari # dalam Python?: ")

options = (("A. Menghapus elemen", "B. Menambah elemen", "C. Menghitung panjang", "D. Mengurutkan"),
           ("A. float", "B. int", "C. str", "D. bool"),
           ("A. 1", "B. 0", "C. 2", "D. Error"),
           ("A. 3", "B. 4", "C. Error", "D. 3.33"),
           ("A. Digunakan untuk mengulang kode", "B. Digunakan untuk komentar", "C. Digunakan untuk menghapus kode", "D. Digunakan untuk input"))

answers = ("C", 'D', "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("_____________________________________")
    print(question)
    for option in options[question_num]:
        print(option)
        
        
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
    
print("==========================")
print("         RESULATS         ")
print("==========================")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")