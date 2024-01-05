import random
from dictionary import dictionary
from decorators import log_performance_to_file, log_random_word, log_game_session, log_learning_session


log_path = 'C:\\...\\...\\....\\GitHub\\Serbian-Words-Game\\log.txt'


@log_learning_session('log.txt')
def start_learning(difficulty):
    num_options = 2 if difficulty == '1' else 3 if difficulty == '2' else 4
    score = 0
    num_questions = 0

    while num_questions < 10:
        word, translation, user_answer, options = ask_question(num_options)
        correct_answer = options.index(translation) + 1
        if user_answer.isdigit() and int(user_answer) == correct_answer:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect. The correct translation is '{translation}'.")
        num_questions += 1

    return score, num_questions


@log_performance_to_file('log.txt')
def generate_random_word():
    return random.choice(list(dictionary.keys()))


# Get the translation of a word from the dictionary
@log_random_word('log.txt')
def get_translation(word):
    return dictionary[word]


# Get a list of options, including the correct answer, for a given translation
@log_performance_to_file('log.txt')
def get_options(translation, num_options):
    options = [translation] + [random.choice(list(dictionary.values())) for _ in range(num_options-1)]
    random.shuffle(options)
    return options


def ask_question(num_options, get_input=input):
    word = generate_random_word()
    translation = get_translation(word)
    options = get_options(translation, num_options)
    print(f"What is the translation of '{word}'?")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    user_answer = get_input("Enter the number of your answer: ")
    return word, translation, user_answer, options


@log_game_session('log.txt')
def main():
    print("Welcome to the Serbian Language Learning Game!")
    difficulty = input("Choose a difficulty level (1, 2, or 3): ")
    score, num_questions = start_learning(difficulty)
    print(f"You got {score} out of {num_questions} correct.")
    if score == 10:
        print("Congratulations, you are fluent in Serbian!")
    else:
        print("Keep practicing to improve your skills.")
    return score, num_questions  # Возвращаем эти значения


if __name__ == "__main__":
    main()
