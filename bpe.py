corpus = ["low", "lower", "newnest", "widest"]

def build_vocab(corpus):
    vocab = {}
    for word in corpus:
        tokens = list(word) + ['</w>']
        word_tuple = tuple(tokens)
        vocab[word_tuple] = vocab.get(word_tuple, 0) + 1
    return vocab

def get_pair_frequencies(vocab):
    pairs = {}
    for word, freq in vocab.items():
        for i in range(len(word)-1):
            pair = (word[i], word[i+1])
            pairs[pair] = pairs.get(pair, 0) + freq
    return pairs

def merge_vocab(pair, vocab):
    new_vocab = {}
    bigram = ''.join(pair)
    for word, freq in vocab.items():
        new_word = []
        i = 0
        while i < len(word):
            if i < len(word) - 1 and (word[i], word[i+1]) == pair:
                new_word.append(bigram)
                i += 2
            else:
                new_word.append(word[i])
                i += 1
        new_vocab[tuple(new_word)] = freq
    return new_vocab

def train_bpe(corpus, num_merges):
    vocab = build_vocab(corpus)
    merges = []
    for _ in range(num_merges):
        pairs = get_pair_frequencies(vocab)
        if not pairs:
            break
        best_pair = max(pairs, key=pairs.get)
        vocab = merge_vocab(best_pair, vocab)
        merges.append(best_pair)
    return merges, vocab

merges, final_vocab = train_bpe(corpus, num_merges=10)
print("Merges learned:")
for m in merges:
    print(m)

print("\nFinal Vocabulary:")
for word in final_vocab:
    print(word)

def apply_bpe(word, merges):
    tokens = list(word) + ['</w>']
    for pair in merges:
        i = 0
        while i < len(tokens) - 1:
            if (tokens[i], tokens[i+1]) == pair:
                tokens[i:i+2] = [''.join(pair)]
            else:
                i += 1
    return tokens

word = "lowest"
tokens = apply_bpe(word, merges)
print(tokens)
