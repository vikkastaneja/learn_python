def sample_function(need_what):
    if need_what == 'integer':
        return 1
    elif need_what == 'string':
        return 'sample'
    elif need_what == 'float':
        return 3.14
    else:
        return 'Not found'


import random
import string

def generate_random_text(min_length, max_length):
    length = random.randint(min_length, max_length)
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

def generate_random_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_random_text_lines(num_words, min_length, max_length):
    words = []
    for _ in range(num_words):
        word_length = random.randint(min_length, max_length)
        words.append(generate_random_word(word_length))
    return ' '.join(words)
