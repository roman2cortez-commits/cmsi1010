import random

# Each template is a dictionary with the story text and who wrote it.
# Words starting with a colon are blanks the player fills in; an
# underscore inside a blank stands for a space in the prompt.
TEMPLATES = [
    {"text": "A :adjective ghost is behind you, holding a :noun.",
     "author": "Roman Cortez"},
    {"text": "Some :adjective :creature with a :weapon is eating "
             ":dessert in the :place.",
     "author": "Roman Cortez"},
    {"text": "Look! There is a :adjective :animal trying to :verb a "
             ":noun in :city.",
     "author": "Roman Cortez"},
    {"text": "Shane Gillis walked on stage holding a :noun and opened "
             "with a joke about :plural_noun. The crowd yelled "
             ":exclamation and threw :food at him.",
     "author": "Roman Cortez"},
    {"text": "The stock market crashed :number percent today after a "
             ":adjective :animal was named CEO of :company.",
     "author": "Roman Cortez"},
    {"text": "My summer internship was :adjective. Every morning I "
             "fetched :number cups of :drink for my :job_title.",
     "author": "Roman Cortez"},
    {"text": "Breaking news: the Federal Reserve raised interest rates "
             "because too many people bought :plural_noun with "
             ":body_part money.",
     "author": "Roman Cortez"},
    {"text": "The new :genre movie stars a :adjective :occupation who "
             "must :verb the :noun before it explodes.",
     "author": "Roman Cortez"},
    {"text": "At the movie premiere, :celebrity tripped on a :noun and "
             "landed in a bucket of :food.",
     "author": "Roman Cortez"},
    {"text": "Tonight only: a :adjective comedy show where every joke is "
             "about :topic and the tickets cost :number dollars.",
     "author": "Roman Cortez"},
    {"text": "I told my finance professor that my portfolio was "
             ":adjective, and he made me calculate the :noun of my "
             ":plural_noun.",
     "author": "Roman Cortez"},
    {"text": "My roommate tried to :verb at the beach in Playa del Rey "
             "and got chased by a :adjective :animal.",
     "author": "Roman Cortez"},
]

# Answers that mean "yes, play again", stored lowercase.
YES_ANSWERS = {"yes", "y", "yeah", "yep", "yup", "sure", "ok", "okay", "bet",
               "sí", "si", "oui"}


def ask_for_word(description):
    """Keep asking until the player types between 1 and 30 characters."""
    article = "an" if description[0] in "aeiou" else "a"
    while True:
        word = input(f"Enter {article} {description}: ").strip()
        if 1 <= len(word) <= 30:
            return word
        print("Please type between 1 and 30 characters.")


def fill_in(template_text):
    """Replace every :blank in the template with a word from the player."""
    finished_words = []
    for word in template_text.split():
        if word.startswith(":"):
            # Keep punctuation like the period in ":noun." after the answer
            name = word[1:].rstrip(".,!?;")
            ending = word[1 + len(name):]
            description = name.replace("_", " ")
            finished_words.append(ask_for_word(description) + ending)
        else:
            finished_words.append(word)
    return " ".join(finished_words)


def play_once():
    """Play one round with a randomly chosen template."""
    template = random.choice(TEMPLATES)
    story = fill_in(template["text"])
    print()
    print(story)
    print()
    print(f"This template was written by {template['author']}.")
    print()
    print()


def main():
    while True:
        play_once()
        answer = input("Do you want to play again? ").strip().lower()
        if answer not in YES_ANSWERS:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
