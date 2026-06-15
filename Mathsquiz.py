import random

def math_quiz():
    score = 0
    questions = 5
    
    for i in range(questions):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 + num2
        
        user_answer = int(input(f"Question {i+1}: {num1} + {num2} = "))
        
        if user_answer == answer:
            score += 1
            print("✓ Correct!")
        else:
            print(f"❌ Wrong! Answer was {answer}")
    
    print(f"\nFinal Score: {score}/{questions}")

math_quiz()