import requests


def get_exchange_rate():
    # Получаем актуальный курс валют с API
    url = "https://api.exchangerate-api.com/v4/latest/RUB"  # Пример API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['rates']['USD']  # Получаем курс доллара к рублю
    else:
        print("Ошибка при получении данных с API.")
        return None


def convert_rub_to_usd(rubles, exchange_rate):
    return rubles * exchange_rate


def main():
    print("Добро пожаловать в конвертер валют!")

    exchange_rate = get_exchange_rate()
    if exchange_rate is None:
        return

    print(f"Актуальный курс: 1 RUB = {exchange_rate} USD")

    while True:
        try:
            rubles = float(input("Введите сумму в рублях для конвертации в доллары (или 'exit' для выхода): "))
            dollars = convert_rub_to_usd(rubles, exchange_rate)
            print(f"{rubles} RUB = {dollars} USD")
        except ValueError:
            print("Выход из программы.")
            break


if __name__ == "__main__":
    main()
