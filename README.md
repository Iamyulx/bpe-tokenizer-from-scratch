# Byte Pair Encoding (BPE) Tokenizer from Scratch

This repository contains a pure Python implementation of a Byte Pair Encoding (BPE) tokenizer built from scratch, without using any external tokenization libraries.

The goal of this project is educational: to understand how subword tokenization works internally in modern NLP systems.

---

## Features

- Vocabulary construction from a raw corpus
- Pair frequency computation
- Iterative merge operations
- Training loop for BPE merges
- Application of learned merges to new words

---

## Example Corpus

```python
corpus = ["low", "lower", "newnest", "widest"]

---

 # Example Output
## Merges Learned

('l', 'o')
('lo', 'w')
('n', 'e')
('s', 't')
('st', '</w>')
('low', '</w>')
('low', 'e')
('lowe', 'r')
('lower', '</w>')
('ne', 'w')

## Final Vocabulary

('low</w>',)
('lower</w>',)
('new', 'ne', 'st</w>')
('w', 'i', 'd', 'e', 'st</w>')

## Applying BPE to a New Word

word = "lowest"
tokens = apply_bpe(word, merges)
print(tokens)

## Example Output

['lowe', 'st</w>']

---

# How it Works

1. Each word is split into characters plus an end-of-word token (</w>).

2. The most frequent adjacent symbol pair is identified.

3. That pair is merged into a new symbol.

4. The process repeats for a fixed number of merges.

5. The learned merges are applied to tokenize new words.

---

