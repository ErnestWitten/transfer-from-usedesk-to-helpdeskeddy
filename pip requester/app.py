import requests
from requests.auth import HTTPBasicAuth

# Константы
USEDESK_API_URL = "..."
HELPDESKEDDY_API_URL = ".../"
USEDESK_API_TOKEN = "..."
HELPDESKEDDY_AUTH = HTTPBasicAuth("...")

def fetch_tickets_from_usedesk():
    """
    Получает список тикетов из Usedesk.
    """
    data = {
        "api_token": USEDESK_API_TOKEN,
        "fstatus": "5"
    }

    try:
        response = requests.get(USEDESK_API_URL, json=data)
        response.raise_for_status()  # Вызывает ошибку, если статус ответа не 200
        tickets = response.json()  # Преобразуем ответ в JSON
        print(f"Успешно получено {len(tickets)} тикетов из Usedesk.")
        return tickets

    except Exception as e:
        print(f"Ошибка при получении тикетов из Usedesk: {e}")
        return []

def create_ticket_in_helpdeskeddy(ticket):
    """
    Создает тикет в Helpdeskeddy.
    """
    form_data = {
        "title": ticket.get("subject", ""),  # Заголовок берется из subject
        "description": ticket.get("last_comment", ""),  # Описание берется из last_comment
        "user_email": ticket.get("channel_email", "")  # Email пользователя
    }

    try:
        response = requests.post(HELPDESKEDDY_API_URL, data=form_data, auth=HELPDESKEDDY_AUTH)
        response.raise_for_status()  # Вызывает ошибку, если статус ответа не 201
        print(f"Тикет '{form_data['title']}' успешно создан в Helpdeskeddy.")
    
    except Exception as e:
        print(f"Ошибка при создании тикета '{form_data['title']}': {e}")

def main():
    """
    Главная функция.
    """
    # Шаг 1: Получение тикетов из Usedesk
    tickets = fetch_tickets_from_usedesk()

    # Шаг 2: Создание тикетов в Helpdeskeddy
    for ticket in tickets:
        create_ticket_in_helpdeskeddy(ticket)

    print("Обработка тикетов завершена.")

if __name__ == "__main__":
    main()
