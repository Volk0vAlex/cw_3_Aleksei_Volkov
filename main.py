from utils import get_data_base, get_filtered_data, get_last_values, get_formatted_data


IGNORE_INCOMPLETE_TRANSACTIONS = True
VALUES_COUNT = 5


def main():
    data = get_data_base()
    data = get_filtered_data(data, ignore_incomplete_transactions=IGNORE_INCOMPLETE_TRANSACTIONS)
    data = get_last_values(data, VALUES_COUNT)
    data = get_formatted_data(data)

    print("INFO: Вывод данных:")
    for transaction in data:
        print(transaction, end="\n")


if __name__ == "__main__":
    main()
