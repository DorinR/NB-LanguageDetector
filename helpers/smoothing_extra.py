

VOCAB_SIZES = {
    0: 26,
    1: 52,
    2: 116766
}


def get_vocab_size(vocab: int, n_gram_size: int, delta: float) -> float:
    extra_value_to_add_to_total = (VOCAB_SIZES[vocab]**n_gram_size)*delta
    return extra_value_to_add_to_total
