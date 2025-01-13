import genanki
import sys

# Установите кодировку для вывода
sys.stdout.reconfigure(encoding='utf-8')
# Создаем модель карточек
model = genanki.Model(
    1607392319,
    'Q&A Model with Options',
    fields=[
        {'name': 'Question'},
        {'name': 'Options'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}<br>{{Options}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ])

questions = []



deck = genanki.Deck(
    2059400110,
    'Python')

# Генерируем карточки
import html

# Генерируем карточки
for qa in questions:
    question_escaped = html.escape(qa["question"])
    options_escaped = html.escape("<br>".join(qa["options"])) if isinstance(qa["options"], list) else html.escape(qa["options"])
    answer_escaped = html.escape(qa["answer"])

    note = genanki.Note(
        model=model,
        fields=[question_escaped, options_escaped, answer_escaped]
    )
    deck.add_note(note)



# Сохраняем файл
genanki.Package(deck).write_to_file('info.apkg')

print("Колода успешно создана: info.apkg")
