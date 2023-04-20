import requests, datetime

def get_data_base(URL):
    try:
        transactions = requests.request("GET", URL, verify=False)
        if transactions.status_code == 200:
            return transactions.json(),"INFO: данные получены успешно\n"
        return None, f"ERROR:status code {transactions.status_code}\n"

    except requests.exceptions.ConnectionError:
        return None, "ERROR: requests.exceptions.ConnectionERROR\n"
    except requests.exceptions.JSONDecodeError:
        return None, "ERROR: requests.exceptions.JSONDecodeError\n"


def get_filtered_data(data, ignore_incomplete_transactions=False):
    data = [item for item in data if "state" in item and item["state"] == "EXECUTED"]
    if ignore_incomplete_transactions:
        data = [item for item in data if "from" in item]
    return data


def get_last_values(data, values_count):
    data = sorted(data, key=lambda item: item["date"], reverse=True)
    data = data[:values_count]
    return data


def get_formatted_data(data):
    formatted_data = list()
    for transaction in data:
        date = datetime.datetime.strptime(transaction["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = transaction["description"]
        from_info, from_bill = "", ""
        if "from" in transaction:
            sender = transaction["from"].split()
            from_bill = sender.pop(-1)
            if "счет" in sender[0].lower():
                from_bill = f"**{from_bill[-4:]}"
            else:
                from_bill = f"{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}"
            from_info = " ".join(sender)
        to = f"{transaction['to'].split()[0]} **{transaction['to'][-4:]}"
        operation_amount = f"{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}"

        formatted_data.append(f"""\
{date} {description}
{from_info} {from_bill} -> {to}
{operation_amount}\n""")
    return formatted_data
