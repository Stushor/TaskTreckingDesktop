# File operating with json-file
import user_list
import json
import task_status
import list_status


def get_data(file_path):
    pass
    # if file_path in user_list:
    #     with open(file_path, "r", encoding="CP1251") as file:
    #         coffee_data = json.load(file)
    #     return coffee_data


def main():
    commands = {
        'list all': list_status.list_all(),
        'list done': list_status.list_done(),
        'list to-do': list_status.list_to_do(),
        'list in progress': list_status.list_in_progress(),
        'add task': task_status.add_task(),
        'update task': task_status.update_task(),
        'delete task': task_status.delete_task(),
        'mark in progress': task_status.mark_in_progress(),
        'mark done': task_status.mark_done()
    }

    # list_user = input('Write here you user list (like ): ')
    # list_data = get_data(list_user)
    flag = True
    while flag:
        print('''
        Operating with your lists:
         |list all|list done|list to-do|list in progress|
        Operating with your tasks:
         |add task|update task|delete task|
        Set status on your tasks:
         |mark in progress|mark done|
        If you want exit:
         |exit|
        ''')
        answer = input('What to do you want? (write here): ')
        if answer == 'exit':
            flag = False
            break
        if answer in commands:
            pass
        else:
            print('Incorrect command entry')
            continue


if __name__ == '__main__':
    main()
