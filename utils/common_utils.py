import random


class CommonUtility:
    @staticmethod
    def get_custom_header():
        header = {"Authorization": "Bearer 37838a5836d84104e99491b431ead98ea4a725b7efbf4129d2614e9bab3663c8",
                  "Content-Type": "application/json"}
        return header

    @staticmethod
    def get_unique_email():
        random_no = random.randint(1000, 99999)
        email = f"test_automation{random_no}@mail.com"
        return email
