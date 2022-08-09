def print_formatted(word, counts):
    print(' {0:18}:{1:>6}'.format(word, counts))

def output_alphabetically(counts):
    print_formatted("words", len(counts))
    print('--------------------------')

    for word, count in dict(sorted(counts.items())).items():
        print_formatted(word, count)


def output_as_is(counts):
    for word, count in counts.items():
        print_formatted(word, count)


def output_sorted_by_value(counts):
    sorted_dict = {}
    sorted_keys = sorted(counts, key=counts.get, reverse=True)

    for w in sorted_keys:
        sorted_dict[w] = counts[w]

    print_formatted("words", len(counts))
    print('--------------------------')

    for word, count in sorted_dict.items():
        print_formatted(word, count)