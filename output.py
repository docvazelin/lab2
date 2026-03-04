def print_results(array, unique_values, counts):
    print("Згенерований масив:")
    print(array)
    print("\nКількість повторень кожного числа:")
    for value, count in zip(unique_values, counts):
        print(f"Число {value}: {count} раз(и)")