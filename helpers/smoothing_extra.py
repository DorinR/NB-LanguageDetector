

VOCAB_SIZES = {
    0: 26,
    1: 52,
    2: 116766
}


def get_smoothing_extra(vocab: int, n_gram_size: int, non_zero_vocab_entries: int) -> float:
    total_possible_n_grams = VOCAB_SIZES[vocab]**n_gram_size
    return total_possible_n_grams - non_zero_vocab_entries
