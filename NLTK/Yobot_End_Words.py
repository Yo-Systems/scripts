#keep track of end words.
end_words = []
for word in words
    if word[-2] in ['.','!','?'] and word != '.':
        end_words.append(word)