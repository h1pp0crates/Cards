def get_symbols_frequency(text):
    result_dict = {}
    tests_len = len(text)
    for symbol in set(text):
        result_dict[symbol] = text.count(symbol) / tests_len
    return result_dict


if __name__ == "__main__":
    print(get_symbols_frequency(""))
