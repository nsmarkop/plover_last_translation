# Plover Last Translation

Macro plugins for [Plover](https://github.com/openstenoproject/plover) to repeat output.

## Installation

Download the latest version of Plover for your operating system from the [releases page](https://github.com/openstenoproject/plover/releases). Only versions 4.0.0.dev6 and higher are supported.

1. Open Plover
2. Navigate to the Plugin Manager tool
3. Select the "plover-last-translation" plugin entry in the list
4. Click install
5. Restart Plover

The same method can be used for updating and uninstalling the plugin.

## Usage

In order to use these plugins you just need to create dictionary entries of the form:

``` json
{
    "example_stroke": "=macro_name:macro_arg1,macro_arg2,..."
}
```

The available macros are:

- repeat_last_translation
    - Arguments
        1. Number of previous translations to output. Default is 1.
- repeat_last_word
    - Arguments
        1. Number of previous words to output. Default is 1.
- repeat_last_fragment
    - Arguments
        1. Number of previous fragments to output. Default is 1.
- repeat_last_character
    - Arguments
        1. Number of previous characters to output. Default is 1.

Some quick examples of the various acceptable forms:

``` json
{
    "1_translation_stroke": "=repeat_last_translation",
    "1_translation_stroke": "=repeat_last_translation:",
    "2_translations_stroke": "=repeat_last_translation:2",
    "5_fragments_stroke": "=repeat_last_fragment:5,"
}
```

For the difference between a word and a fragment, see the [RetroFormatter documentation](https://github.com/openstenoproject/plover/blob/d5c8e45d0cb398baee8b7ea1f81d7c998143361f/plover/formatting.py#L91).
