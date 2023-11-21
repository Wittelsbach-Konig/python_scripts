import csv
import os


def generate_users_data(count, json_body, csv_name):
    """Generate csv file"""
    fieldnames = list(json_body.keys())
    csv_folder = 'tmp'
    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)

    csv_path = os.path.join(csv_folder, csv_name)
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()

        for _ in range(count):
            user_data = json_body.copy()
            user_data['login'] = f'user_{_}'

            writer.writerow(user_data)


if __name__ == '__main__':
    user_count = 1000
    csv_folder = '/tmp/'
    json_body = {
        "login": "testUser",
        "password": "testpassword",
        "confirmPassword": "testpassword",
        "email": "user@example.com",
        "firstName": "Vladimir",
        "lastName": "Putin",
        "address": "Kremlin",
        "roles": [
            "DETECTIVE",
        ],
        "telegramId": 12346,
    }
    generate_users_data(user_count, json_body,
                        csv_name='user_registration.csv')
    json_body = {
        "login": "testUser1",
        "password": "testpassword"
    }
    generate_users_data(user_count, json_body,
                        csv_name='user_login.csv')
