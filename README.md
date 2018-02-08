# Plover Last Translation

Macro plugin for [Plover](https://github.com/openstenoproject/plover) to repeat the last translation.

## Installation

Download the latest version of Plover for your operating system from the [releases page](https://github.com/openstenoproject/plover/releases). Only versions 4.0.0.dev6 and higher are supported.

1. Open Plover
2. Navigate to the Plugin Manager tool
3. Select the "plover-last-translation" plugin entry in the list
4. Click install
5. Restart Plover

The same method can be used for updating and uninstalling the plugin.

## Usage

In order to use this plugin you just need to create a dictionary entry of the form:

``` json
{
    "example_stroke": "=repeat_last_translation"
}
```
