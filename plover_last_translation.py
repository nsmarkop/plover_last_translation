'''
Functionality to repeat the last translation output in Plover.
'''

from plover.translation import Translator, Translation, Stroke


def repeat_last_translation(translator: Translator, stroke: Stroke, macro_args: str) -> None:
    '''
    Macro to repeat the last transition in Plover.

    :param translator: The active Plover translator that is executing the macro.
    :type translator: plover.translation.Translator

    :param stroke: The current stroke (what invoked this macro).
    :type stroke: plover.translation.Stroke

    :param macro_args: The optional arguments specified to the macro.
    :type macro_args: str
    '''

    translations = translator.get_state().translations
    if not translations:
        return

    last_translation = translations[-1]
    repeated_translation = Translation(last_translation.strokes, last_translation.english)
    
    translator.translate_translation(repeated_translation)
