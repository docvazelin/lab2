import output
import prog_input
import solution

def main():
    arr = prog_input.prog_input()
    unique_vals, counts = solution.count_occurrences(arr)
    output.print_results(arr, unique_vals, counts)


if __name__ == "__main__":
    main()