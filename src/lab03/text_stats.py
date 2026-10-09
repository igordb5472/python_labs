from ..lib.text import normalize, tokenize, count_freq, top_n

text = input()
tokens = tokenize(normalize(text))
print(f'Всего слов: {len(tokens)}')
unique_tokens = set(tokens)
print(f'Уникальных слов: {len(unique_tokens)}')
top = top_n(count_freq(tokens), 5)
print(f'Топ-5:')
for x, y in top:
    print(f'{x}:{y}')