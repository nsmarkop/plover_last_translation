'''
Functionality to repeat output in Plover.
'''

from plover.translation import Translator, Translation, Stroke
from plover.formatting import RetroFormatter


DELIM_ARGS = ','

def repeat_last_translation(translator: Translator, stroke: Stroke, args: str) -> None:
    '''
    Macro to repeat the last translation(s) in Plover.

    :param translator: The active Plover translator that is executing the macro.
    :param stroke: The current stroke (what invoked this macro).
    :param args: The optional arguments specified to the macro as a comma-delimited string.
                 Piece 1: The number of previous translations to repeat. Default is 1.
    '''

    # Get the current state
    translations = translator.get_state().translations
    if not translations:
        return

    # Process input
    try:
        num_to_repeat = int(args.split(DELIM_ARGS)[0])
    except:
        num_to_repeat = 1

    # Output the new translations
    for translation in translations[-num_to_repeat:]:
        repeated_translation = Translation(translation.strokes, translation.english)
        translator.translate_translation(repeated_translation)

def repeat_last_word(translator: Translator, stroke: Stroke, args: str) -> None:
    '''
    Macro to repeat the last word(s) in Plover.

    :param translator: The active Plover translator that is executing the macro.
    :param stroke: The current stroke (what invoked this macro).
    :param args: The optional arguments specified to the macro as a comma-delimited string.
                 Piece 1: The number of previous words to repeat. Default is 1.
    '''

    # Get the current state
    translations = translator.get_state().translations
    if not translations:
        return

    # Process input
    try:
        num_to_repeat = int(args.split(DELIM_ARGS)[0])
    except:
        num_to_repeat = 1

    # Output the new translations
    formatter = RetroFormatter(translations)
    last_words = formatter.last_words(num_to_repeat)

    for word in last_words:
        new_translation = Translation([stroke], word)
        translator.translate_translation(new_translation)

def repeat_last_fragment(translator: Translator, stroke: Stroke, args: str) -> None:
    '''
    Macro to repeat the last fragments(s) in Plover.

    :param translator: The active Plover translator that is executing the macro.
    :param stroke: The current stroke (what invoked this macro).
    :param args: The optional arguments specified to the macro as a comma-delimited string.
                 Piece 1: The number of previous fragments to repeat. Default is 1.
    '''

    # Get the current state
    translations = translator.get_state().translations
    if not translations:
        return

    # Process input
    try:
        num_to_repeat = int(args.split(DELIM_ARGS)[0])
    except:
        num_to_repeat = 1

    # Output the new translations
    formatter = RetroFormatter(translations)
    last_fragments = formatter.last_fragments(num_to_repeat)

    for fragment in last_fragments:
        new_translation = Translation([stroke], fragment)
        translator.translate_translation(new_translation)

def repeat_last_character(translator: Translator, stroke: Stroke, args: str) -> None:
    '''
    Macro to repeat the last character(s) in Plover.

    :param translator: The active Plover translator that is executing the macro.
    :param stroke: The current stroke (what invoked this macro).
    :param args: The optional arguments specified to the macro as a comma-delimited string.
                 Piece 1: The number of previous characters to repeat. Default is 1.
    '''

    # Get the current state
    translations = translator.get_state().translations
    if not translations:
        return

    # Process input
    try:
        num_to_repeat = int(args.split(DELIM_ARGS)[0])
    except:
        num_to_repeat = 1

    # Output the new translation
    formatter = RetroFormatter(translations)
    last_text = formatter.last_text(num_to_repeat)

    new_translation = Translation([stroke], last_text)
    translator.translate_translation(new_translation)
