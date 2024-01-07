import random
from dictionary import dictionary


def generate_random_translation(dictionary):
    while True:
        word = random.choice(list(dictionary.keys()))
        translation = dictionary[word]
        yield word, translation


random_translation_generator = generate_random_translation(dictionary)
for _ in range(5):
    word, translation = next(random_translation_generator)
    print(f"{word} - {translation}")
  
