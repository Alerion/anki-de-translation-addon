set dotenv-load

check-code:
    uv run ruff format
    uv run ruff check --fix
    mypy

start-anki:
    $ANKI_FOLDER/anki-console.exe

create-addon-symlink:
    @echo "Run this in windows terminal in administrator mode:"
    @echo "mklink /D $(echo $ANKI_ADDONS_FOLDER/addons21/deutsch_anki_addon | tr '/' '\\') $(pwd | tr '/' '\\')\\addon\\"

install-dependencies-for-anki:
    uv pip install --group addon --target ./addon/dependencies
