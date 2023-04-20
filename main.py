from utils import get_data_base, get_filtered_data, get_last_values, get_formatted_data

IGNORE_INCOMPLETE_TRANSACTIONS = True
URL = "https://www.jsonkeeper.com/b/YKDP"
VALUES_COUNT = 5

def main():
    data, info = get_data_base(URL)
    if not data:
        exit(info)
    else:
        print(info)

    data = get_filtered_data(data, ignore_incomplete_transactions = IGNORE_INCOMPLETE_TRANSACTIONS)
    data = get_last_values(data, VALUES_COUNT)
    data = get_formatted_data(data)

    print("INFO: Вывод данных:")
    for transaction in data:
        print(transaction, end="\n")

if __name__ == "__main__":
    main()
