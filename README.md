# TaskTreckingDesktop
https://roadmap.sh/projects/task-tracker
[ENG]

Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line 
interface (CLI) to track what you need to do, what you have done, and what you are currently working on. This project 
will help you practice your programming skills, including working with the filesystem, handling user inputs, and
building a simple CLI application.

## Requirements
The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in
a JSON file. The user should be able to:

- Add, Update, and Delete tasks
- Mark a task as in progress or done
- List all tasks
- List all tasks that are done
- List all tasks that are not done
- List all tasks that are in progress

Here are some constraints to guide the implementation:

- You can use any programming language to build this project.
- Use positional arguments in command line to accept user inputs.
- Use a JSON file to store the tasks in the current directory.
- The JSON file should be created if it does not exist.
- Use the native file system module of your programming language to interact with the JSON file.
- Do not use any external libraries or frameworks to build this project.
- Ensure to handle errors and edge cases gracefully.
## Example
The list of commands and their usage is given below:
```python
# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
```
## Task Properties
Each task should have the following properties:

- id: A unique identifier for the task
- description: A short description of the task
- status: The status of the task (todo, in-progress, done)
- createdAt: The date and time when the task was created
- updatedAt: The date and time when the task was last updated 
Make sure to add these properties to the JSON file when adding a new task and update them when updating a task.

## Getting Started
Here are a few steps to help you get started with the Task Tracker CLI project:

### Set Up Your Development Environment
- Choose a programming language you are comfortable with (e.g., Python, JavaScript, etc.).
- Ensure you have a code editor or IDE installed (e.g., VSCode, PyCharm).
### Project Initialization
- Create a new project directory for your Task Tracker CLI.
- Initialize a version control system (e.g., Git) to manage your project.
### Implementing Features
- Start by creating a basic CLI structure to handle user inputs.
- Implement each feature one by one, ensuring to test thoroughly before moving to the next e.g. implement adding task
functionality first, listing next, then updating, marking as in progress, etc.
### Testing and Debugging
- Test each feature individually to ensure they work as expected. Look at the JSON file to verify that the tasks are
being stored correctly.
- Debug any issues that arise during development.
### Finalizing the Project
- Ensure all features are implemented and tested.
- Clean up your code and add comments where necessary.
- Write a good readme file on how to use your Task Tracker CLI.
By the end of this project, you will have developed a practical tool that can help you or others manage tasks
efficiently. This project lays a solid foundation for more advanced programming projects and real-world applications.

Happy coding!

-----

[RU]

Task tracker — это проект, используемый для отслеживания и управления вашими задачами. В этом задании вы создадите 
простой интерфейс командной строки (CLI) для отслеживания того, что вам нужно сделать, что вы сделали и над чем вы
сейчас работаете. Этот проект поможет вам практиковать свои навыки программирования, включая работу с файловой системой,
обработку ввода пользователя и создание простого приложения CLI.

## Требования
Приложение должно запускаться из командной строки, принимать действия и ввод пользователя в качестве аргументов
и сохранять задачи в файле JSON. Пользователь должен иметь возможность:

- Добавить, обновить и удалить задачи
- Отметить задачу как выполняемую или выполненную
- Список всех задач
- Список всех выполненных задач
- Список всех невыполненных задач
- Список всех выполняемых задач

Вот некоторые ограничения, которые помогут вам в реализации:

- Для сборки этого проекта можно использовать любой язык программирования.
- Используйте позиционные аргументы в командной строке для приема ввода данных пользователем.
- Используйте файл JSON для хранения задач в текущем каталоге.
- Файл JSON следует создать, если он не существует.
- Используйте собственный модуль файловой системы вашего языка программирования для взаимодействия с файлом JSON.
- Не используйте внешние библиотеки или фреймворки для сборки этого проекта.
- Убедитесь, что ошибки и пограничные случаи обрабатываются корректно.

## Пример
Список команд и их использование приведены ниже:
```python
# Добавление новой задачи
task-cli add "Купить продукты"
# Вывод: Задача успешно добавлена (ID: 1)

# Обновление и удаление задач
task-cli update 1 "Купить продукты и приготовить ужин"
task-cli delete 1

# Отметка задачи как выполняемой или выполненной
task-cli mark-in-progress 1
task-cli mark-done 1

# Список всех задач
task-cli list

# Список задач по статусу
task-cli list done
task-cli list todo
task-cli list in-progress
```
## Свойства задачи
Каждая задача должна иметь следующие свойства:

- id: уникальный идентификатор задачи
- description: краткое описание задачи
- status: статус задачи (todo, in-progress, done)
- createdAt: дата и время создания задачи
- updatedAt: дата и время последнего обновления задачи
Обязательно добавьте эти свойства в файл JSON при добавлении новой задачи и обновите их при обновлении задачи.

## Начало работы
Вот несколько шагов, которые помогут вам начать работу с проектом Task Tracker CLI:

### Настройка среды разработки
- Выберите язык программирования, с которым вам удобно работать (например, Python, JavaScript и т. д.).
- Убедитесь, что у вас установлен редактор кода или IDE (например, VSCode, PyCharm).
### Инициализация проекта
- Создайте новый каталог проекта для Task Tracker CLI.
- Инициализируйте систему контроля версий (например, Git) для управления вашим проектом.
### Реализация функций
- Начните с создания базовой структуры CLI для обработки ввода данных пользователем.
- Реализуйте каждую функцию одну за другой, тщательно протестировав ее перед переходом к следующей, например, сначала добавьте функциональность задачи, затем перечислите, затем обновите, отметьте как выполняемую и т. д.
### Тестирование и отладка
- Протестируйте каждую функцию по отдельности, чтобы убедиться, что она работает так, как ожидается. Посмотрите на файл JSON, чтобы убедиться, что задачи
сохраняются правильно.
- Отладьте все проблемы, возникающие в процессе разработки.
### Завершение проекта
- Убедитесь, что все функции реализованы и протестированы.
- Очистите свой код и добавьте комментарии, где это необходимо.
- Напишите хороший файл readme о том, как использовать ваш CLI Task Tracker.
К концу этого проекта вы разработаете практический инструмент, который поможет вам или другим эффективно управлять задачами. Этот проект закладывает прочную основу для более сложных проектов программирования и реальных приложений.

Приятного кодирования!