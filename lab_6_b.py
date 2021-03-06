"""Задача. Вивести дані про працівників старших 30-ти років, які не мають вищої
освіти. Поля структури: Прізвище, Вік, Освіта, Посада.
"""
workers = [
    {
        'Прізвище': 'Опанасенко',
        'Вік': 33,
        'Освіта': 'середня',
        'Посада': 'технічний працівник',
    },

    {
        'Прізвище': 'Романенко',
        'Вік': 21,
        'Освіта': 'вища',
        'Посада': 'економіст',
    },

    {
        'Прізвище': 'Старозубов',
        'Вік': 56,
        'Освіта': 'початкова',
        'Посада': 'сторож',
    },

    {
        'Прізвище': 'Матросова',
        'Вік': 39,
        'Освіта': 'середня',
        'Посада': 'завгосп',
    },

    {
        'Прізвище': 'Кліменко',
        'Вік': 29,
        'Освіта': 'вища',
        'Посада': 'системний адміністратор',
    },

    {
        'Прізвище': 'Данилова',
        'Вік': 31,
        'Освіта': 'вища',
        'Посада': 'бухгалтер',
    },

    {
        'Прізвище': 'Галушко',
        'Вік': 36,
        'Освіта': 'вища',
        'Посада': 'менеджер',
    },
]

print('Працівники, яким більше 30 років і немає віщої освіти:')
for worker in workers:
    if worker['Вік'] > 30 and worker['Освіта'] != 'вища':
        print()
        for key, value in worker.items():
            print(f'{key}: {value}')
