'''
Functionality to repeat output in Plover.
'''

from typing import List

from plover.translation import Translation
from plover.formatting import _Context, _Action


DELIM_ARGS = ','

def repeat_last_translation(context: _Context, args: str) -> _Action:
    '''
    Meta to repeat the last translation(s) in Plover.

    :param context: The context of actions in Plover.
    :param args: Optional arguments provided to the meta as a comma-delimited string.
                 Piece 1: The number of previous translations to repeat. Default is 1.

    :return: The next action for Plover to perform.
    '''

    # Process input
    try:
        num_to_repeat = int(args.split(DELIM_ARGS)[0])
    except:
        num_to_repeat = 1

    output = ''
    translations: List[Translation] = context.previous_translations[-num_to_repeat:]
    for translation in translations:
        actions: List[_Action] = reversed(translation.formatting)
        for action in actions:
            output = output + action.text

    # Create the new action
    action: _Action = context.new_action()
    action.text = output

    return action

def repeat_last_word(context: _Context, args: str) -> _Action:
    '''
    Meta to repeat the last word(s) in Plover.

    :param context: The context of actions in Plover.
    :param args: Optional arguments provided to the meta as a comma-delimited string.
                 Piece 1: The number of previous words to repeat. Default is 1.

    :return: The next action for Plover to perform.
    '''

    # Process input
    try:
        num_to_repeat = int(args.split(DELIM_ARGS)[0])
    except:
        num_to_repeat = 1

    words = context.last_words(count=num_to_repeat)

    # Create the new action
    action: _Action = context.new_action()
    action.text = ''.join(words)

    return action

def repeat_last_fragment(context: _Context, args: str) -> _Action:
    '''
    Meta to repeat the last fragments(s) in Plover.

    :param context: The context of actions in Plover.
    :param args: Optional arguments provided to the meta as a comma-delimited string.
                 Piece 1: The number of previous fragments to repeat. Default is 1.

    :return: The next action for Plover to perform.
    '''

    # Process input
    try:
        num_to_repeat = int(args.split(DELIM_ARGS)[0])
    except:
        num_to_repeat = 1

    fragments = context.last_fragments(count=num_to_repeat)

    # Create the new action
    action: _Action = context.new_action()
    action.text = ''.join(fragments)

    return action

def repeat_last_character(context: _Context, args: str) -> _Action:
    '''
    Meta to repeat the last character(s) in Plover.

    :param context: The context of actions in Plover.
    :param args: Optional arguments provided to the meta as a comma-delimited string.
                 Piece 1: The number of previous characters to repeat. Default is 1.

    :return: The next action for Plover to perform.
    '''

    # Process input
    try:
        num_to_repeat = int(args.split(DELIM_ARGS)[0])
    except:
        num_to_repeat = 1

    text = context.last_text(num_to_repeat)

    # Create the new action
    action: _Action = context.new_action()
    action.text = text

    return action
