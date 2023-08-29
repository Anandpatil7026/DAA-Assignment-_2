def search(pattern, text):
    pattern_length = len(pattern)
    text_length = len(text)
    pattern_hash = sum(ord(pattern[i]) for i in range(pattern_length))
    text_hash = sum(ord(text[i]) for i in range(pattern_length))

    for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+pattern_length]:
                return i

        if i < text_length - pattern_length:
            text_hash = text_hash - ord(text[i]) + ord(text[i+pattern_length])

    return -1

text = "Hello, world!"
pattern = "world"
index = search(pattern, text)
if index != -1:
    print("Pattern found at index", index)
else:
    print("Pattern not found in the text")
