# for i in range(1, 6, 2):
#     print(i)



# issheright = True
# while issheright:
#     if input("Какое мое любимое блюдо:") == "Плов":
#         issheright = False
#         print("Молодец!))")
#     else :
#         print("Попробуй еще раз")

# n  = int(input("Enter length:"))
# user_list = []

# i = 0
# while i < n:
#     string = "Enter element #" + str(i + 1) + ": "
#     user_list.append(input(string))
#     i += 1
# print(user_list)


questions = [
    ("1. Какое мое любимое блюдо?", "Плов"),
    ("2. Какой мой любимый цвет?", "Зеленый"),
    ("3. Мое любимое время года?", "Осень"),
    ("4. Сладкое или соленое?", "Сладкое"),
    ("5. Кошка или собака?", "Кошка"),
    ("6. Любимый напиток?", "Чай"),
    ("7. Кино или книги?", "Книги"),
    ("8. Гулять или остаться дома?", "Остаться дома"),
]

score = 0

for question, correct_answer in questions:
    user_answer = input(f"{question}")
    if user_answer.strip().lower() == correct_answer.lower():
        print("Правильно! \n") 
        score += 1
    else:
        print(f"Не правильно! Правильный ответ: {correct_answer}\n")
print(f"Игра завершена! Правильных ответов: {score} из 8.")
















