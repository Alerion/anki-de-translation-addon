# Mark Deutch with colors

## Hotkeys

- ``F1`` - generate Anki card for copied word. Use ``F12`` in Edit card window.
- ``F2`` - color translation and makes text bold.
- ``F3`` - insert "der".
- ``F4`` - insert "die".
- ``F5`` - insert "das".
- ``F6`` - insert "NOUN".
- ``F7`` - insert "VERB".
- ``F8`` - insert "ADJECTIVE".
- ``F9`` - insert "ADVERB".
- ``F10`` - insert "PRONOUN".

## Install

Install dependencies:

    uv sync
    . .venv/Scripts/activate

Copy and edit .env file:

    cp .env.template .env

Create symlink to addons folder following instruction from:

    just create-addon-symlink

Install dependencies into addon folder

    just install-dependencies-for-anki

Run anki in console:

    just start-anki

Edit addon config in Anki UI: Tools -> Add-ons -> deutsch_anki_addon -> Config

## Development

Install pre-commit hooks:

    uvx pre-commit install

Format and check code:

    just check-code
