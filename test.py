lang_choice = input('Какой язык предпочитаете? What language would you choose? ')
if lang_choice.lower == 'english' or lang_choice.lower == 'английский':
    from ENG import *
elif lang_choice.lower() == 'russian' or lang_choice.lower == 'русский':
    from RUS import *

print(lang_choice.lower())