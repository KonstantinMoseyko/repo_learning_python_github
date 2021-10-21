# 6_3

from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users_full_name_file:
    with open('hobby.csv', 'r', encoding='utf-8') as users_hobby_file:
        if len(users_full_name_file.readlines()) >= len(users_hobby_file.readlines()):
            users_full_name_file.seek(0)
            users_hobby_file.seek(0)
            with open('users_hobby.csv', 'w', encoding='utf-8') as users_full_name_hobby_file:
                users_full_name_list = [name.strip() for name in users_full_name_file]
                users_hobby_file_list = [hobby.strip() for hobby in users_hobby_file]
                users_hobby_dict = {key: val for key, val in zip_longest(users_full_name_list, users_hobby_file_list)}
                print(users_hobby_dict, file=users_full_name_hobby_file)
        else:
            exit(1)
