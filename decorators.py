import functools
import time
from datetime import datetime


def log_performance_to_file(log_file_path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(log_file_path, 'a', encoding='utf-8') as log_file:
                log_file.write(f"Timestamp: {timestamp}\n")
                log_file.write(f"Function: {func.__name__}\n")
                log_file.write(f"Arguments: {args if args else ''} {kwargs if kwargs else ''}\n")
                log_file.write(f"Result: {result}\n")
                log_file.write(f"Executed in: {end_time - start_time:.4f} seconds\n")
                log_file.write("--------------------------------------------------\n")
            return result
        return wrapper
    return decorator


def log_random_word(log_file_path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(log_file_path, 'a', encoding='utf-8') as log_file:
                log_file.write(f"Timestamp: {timestamp}\n")
                log_file.write(f"Random Word Generated: {result}\n")
                log_file.write("--------------------------------------------------\n")
            return result
        return wrapper
    return decorator


def log_game_session(log_file_path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            score, num_questions = func(*args, **kwargs)
            end_time = time.time()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(log_file_path, 'a', encoding='utf-8') as log_file:
                log_file.write(f"Timestamp: {timestamp}\n")
                log_file.write(f"Total Game Time: {end_time - start_time:.4f} seconds\n")
                log_file.write(f"Final Score: {score}/{num_questions}\n")
                log_file.write("--------------------------------------------------\n")
            return score, num_questions
        return wrapper
    return decorator


def log_learning_session(log_file_path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            score, num_questions = func(*args, **kwargs)
            end_time = time.time()
            with open(log_file_path, 'a') as log_file:
                log_file.write(f"\n--- Learning Session Started: {datetime.now()} ---\n")
                log_file.write(f"Total Questions: {num_questions}, Correct Answers: {score}\n")
                log_file.write(f"Session Ended: {datetime.now()} | Total Duration: {end_time - start_time:.2f} seconds\n")
                log_file.write("--- End of Learning Session ---\n\n")
            return score, num_questions
        return wrapper
    return decorator


def log_generated_items(log_file_path):
    def decorator(generator_func):
        @functools.wraps(generator_func)
        def wrapper(*args, **kwargs):
            gen = generator_func(*args, **kwargs)
            while True:
                try:
                    word, translation = next(gen)
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open(log_file_path, 'a', encoding='utf-8') as log_file:
                        log_file.write(f"{timestamp} - Generated word: '{word}', Translation: '{translation}'\n")
                    yield word, translation
                except StopIteration:
                    break
        return wrapper
    return decorator

  
