def respace_text(text, block_length):
    return [text[i:i+block_length] for i in range(0, len(text), block_length)]
