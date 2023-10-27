def sorted_fruts(fruts):
    fruts_dict = dict(fruts)
    sorted_fruts = sorted(fruts_dict.items(), key=lambda item: item[1])
    return sorted_fruts


fruts = [("apple", 2.5), ("banana", 3.5), ("orange", 1.5)]
print(sorted_fruts(fruts))
