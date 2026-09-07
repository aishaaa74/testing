import random
 
MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 10
 
 
def parse_guess(user_input: str) -> int:
   
    user_input = user_input.strip()
 
    if not user_input or not (
        user_input.isdigit()
        or (user_input.startswith("-") and user_input[1:].isdigit())
    ):
        raise ValueError(f"'{user_input}' не является целым числом")
 
    return int(user_input)
 
 
def is_in_range(number: int, low: int = MIN_NUMBER, high: int = MAX_NUMBER) -> bool:
    """Проверяет, что число находится в допустимом диапазоне [low, high]."""
    return low <= number <= high
 
 
def check_guess(guess: int, secret: int) -> str:
  
    if guess == secret:
        return "equal"
    elif guess < secret:
        return "greater"
    else:
        return "less"
 
 
class GuessNumberGame:

 
    def __init__(self, secret: int = None, max_attempts: int = MAX_ATTEMPTS):
        self.secret = secret if secret is not None else random.randint(MIN_NUMBER, MAX_NUMBER)
        self.max_attempts = max_attempts
        self.attempts_used = 0
        self.is_finished = False
        self.is_won = False
 
    def make_guess(self, user_input: str) -> dict:
      
        if self.is_finished:
            return {"status": "error", "message": "Игра уже завершена"}
 
        try:
            guess = parse_guess(user_input)
        except ValueError as e:
            # Некорректный ввод не тратит попытку
            return {"status": "error", "message": str(e)}
 
        if not is_in_range(guess):
            return {
                "status": "error",
                "message": f"Число должно быть от {MIN_NUMBER} до {MAX_NUMBER}",
            }
 
        self.attempts_used += 1
        result = check_guess(guess, self.secret)
 
        if result == "equal":
            self.is_finished = True
            self.is_won = True
 
        attempts_left = self.max_attempts - self.attempts_used
        if attempts_left <= 0 and result != "equal":
            self.is_finished = True
 
        return {
            "status": "ok",
            "result": result,
            "attempts_left": attempts_left,
            "won": self.is_won,
        }
 
 
def main():
    game = GuessNumberGame()
 
    print("=" * 40)
    print("Добро пожаловать в игру 'Угадай число'!")
    print(f"Я загадал число от {MIN_NUMBER} до {MAX_NUMBER}.")
    print(f"У тебя есть {MAX_ATTEMPTS} попыток, чтобы его угадать.")
    print("=" * 40)
 
    while not game.is_finished:
        user_input = input(f"\nПопытка {game.attempts_used + 1}/{game.max_attempts}. Введи число: ")
        outcome = game.make_guess(user_input)
 
        if outcome["status"] == "error":
            print(outcome["message"])
            continue
 
        if outcome["result"] == "equal":
            print(f"\n🎉 Поздравляю! Ты угадал число {game.secret} "
                  f"за {game.attempts_used} попыток(-ку)!")
        elif outcome["result"] == "greater":
            print("Загаданное число БОЛЬШЕ, чем ты назвал.")
        else:
            print("Загаданное число МЕНЬШЕ, чем ты назвал.")
 
        if game.is_finished and not game.is_won:
            print(f"\n Увы, попытки закончились. Загаданное число было: {game.secret}.")
 
    print("\nСпасибо за игру!")
 
 
if __name__ == "__main__":
    main()