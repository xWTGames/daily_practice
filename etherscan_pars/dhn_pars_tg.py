import requests
import time
from web3 import Web3

# 🔹 Налаштування
ETHERSCAN_API_KEY = "BPBRPARV6AT5I2R7QS6YT9UWPD18S8T2ZE"  # Встав свій API-ключ
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Встав Infura ID
TOKEN_ADDRESS = "0x32462ba310e447ef34ff0d15bce8613aa8c4a244"  # Токен, який моніторимо
TELEGRAM_API_TOKEN = "8004232894:AAFjXyNlSMauTvSKqvbEuNNkjHJXTesnxSM"  # Встав токен твого бота
TELEGRAM_CHAT_ID = "-1002613956692"  # Встав Chat ID

# 🔹 Підключення до Ethereum
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# 🔹 Остання перевірена транзакція
last_checked_tx = None

def send_telegram_message(message):
    """Відправляє повідомлення в Telegram"""
    url = f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

def get_latest_transactions(token_address, api_key):
    """Отримує всі останні операції токена"""
    params = {
        "module": "account",
        "action": "tokentx",
        "contractaddress": token_address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "desc",
        "apikey": api_key
    }

    response = requests.get("https://api.etherscan.io/api", params=params)
    data = response.json()

    if data["status"] == "1":
        return data["result"]
    else:
        print("Помилка:", data["message"])
        return []

def monitor_transactions():
    """Безперервний моніторинг нових операцій"""
    global last_checked_tx

    while True:
        transactions = get_latest_transactions(TOKEN_ADDRESS, ETHERSCAN_API_KEY)

        if transactions:
            if last_checked_tx is None:
                last_checked_tx = transactions[0]["hash"]  # Запам'ятовуємо останню відому транзакцію
                continue

            new_transactions = []

            for tx in transactions:
                if tx["hash"] == last_checked_tx:
                    break  # Всі нові вже обробили
                new_transactions.append(tx)

            if new_transactions:
                print(f"🔹 Знайдено {len(new_transactions)} нових операцій!")
                find = (f"🔹 Знайдено {len(new_transactions)} нових операцій!")
                send_telegram_message(find)

                for tx in reversed(new_transactions):  # Від старих до нових
                    amount = web3.from_wei(int(tx['value']), 'ether')
                    message = (
                        f"🔹 *Нова транзакція!*\n"
                        f"🔹 *TxHash:* `{tx['hash']}`\n"
                        f"🔹 *Відправник:* `{tx['from']}`\n"
                        f"🔹 *Отримувач:* `{tx['to']}`\n"
                        f"🔹 *Кількість:* `{amount}` токенів\n"
                        f"🔹 *Час:* {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(tx['timeStamp'])))}"
                    )
                    send_telegram_message(message)
                    print(message)

                last_checked_tx = new_transactions[0]["hash"]  # Оновлюємо останню перевірену транзакцію

        time.sleep(30)  # Перевіряти кожні 30 секунд

# Запуск моніторингу
monitor_transactions()
