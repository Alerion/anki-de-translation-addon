import aqt.editor
from aqt.utils import showInfo

from .. import wiktionary


def insert_audio(editor: aqt.editor.Editor) -> None:
    clipboard = editor.mw.app.clipboard()
    if clipboard is None:
        showInfo("Clipboard is not available")
        return
    word = clipboard.text().strip()

    if not word:
        showInfo("No word found in clipboard")
        return

    page = wiktionary.find_word_page(word)
    if not page:
        showInfo(f"Page not found for word '{word}'")
        return

    wikitext = wiktionary.get_page_wikitext(page.page_id)
    if not wikitext:
        showInfo(f"No wikitext found for: {word}")
        return

    audio_url = wiktionary.get_audio_url_from_wikitext(wikitext)
    if not audio_url:
        showInfo(f"Audio file was not found for: {word}")
        return

    clipboard.setText(audio_url)
    # Trigger audio paste, so Anki can replace with proper tag.
    editor.onPaste()
    clipboard.setText(word)
