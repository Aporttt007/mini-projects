import genanki

# Define a unique model for your deck
my_model = genanki.Model(
    1607392319,  # Unique model ID
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',  # Front of the card
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',  # Back of the card
        },
    ],
)

# Create a new deck
my_deck = genanki.Deck(
    2059400110,  # Unique deck ID
    'Politica',  # Deck name
)

questions = [
  {
    "question": "Democratization",
    "answer": "Taking into account public opinion in solving state and public affairs: improving the electoral system"
  }, 
]


for q in questions:
    note = genanki.Note(
        model=my_model,
        fields=[q['question'], q['answer']]
    )
    my_deck.add_note(note)

# Export the deck to a .apkg file
genanki.Package(my_deck).write_to_file('political_science_questions.apkg')

print("Anki deck created: political_science_questions.apkg")
