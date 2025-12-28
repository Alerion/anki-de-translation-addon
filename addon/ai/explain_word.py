from functools import cache

from aqt import mw
from google import genai
from pydantic import BaseModel, Field

from ..enums import SpeachPart
from .prompt_utils import load_prompt_template_from_file, replace_promt_placeholder

GOOGLE_MODEL = "gemini-2.5-flash"


class Synonym(BaseModel):
    word: str = Field(description="The synonym word.")
    difference: str = Field(
        description="A brief explanation of how this synonym differs from the original word."
    )


class ExplainWordResponse(BaseModel):
    ukrainian_translation: str = Field(description="The Ukrainian translation of the word.")
    additional_context: str = Field(description="Additional context or explanation about the word.")
    usage_examples: list[str] = Field(
        description="A list of example sentences demonstrating the usage of the word."
    )
    synonyms: list[Synonym] = Field(description="A list of synonyms for the word.")
    additional_info: list[str] = Field(
        description="Any additional relevant information about the word."
    )


def explain_word_with_ai(word: str, part_of_speech: SpeachPart) -> ExplainWordResponse:
    explain_word_prompt_template = get_explain_word_prompt()
    explain_word_prompt_params = {
        "word": word,
        "part_of_speech": part_of_speech.value,
    }
    explain_word_prompt = explain_word_prompt_template % explain_word_prompt_params

    response = get_genai_client().models.generate_content(
        model=GOOGLE_MODEL,
        config=genai.types.GenerateContentConfig(
            response_mime_type="application/json",
            response_json_schema=ExplainWordResponse.model_json_schema(),
            temperature=0.7,
        ),
        contents=explain_word_prompt,
    )

    generate_sentence_response = ExplainWordResponse.model_validate_json(response.text or "")
    return generate_sentence_response


@cache
def get_explain_word_prompt() -> str:
    return replace_promt_placeholder(load_prompt_template_from_file("explain_word.txt"))


@cache
def get_genai_client() -> genai.Client:
    config = mw.addonManager.getConfig(__name__)
    if config is None:
        raise ValueError("Config is not available")

    api_key = config.get("GENAI_API_KEY", "")
    if not api_key:
        raise ValueError("GenAI API key is not set in the addon configuration")
    client = genai.Client(api_key=api_key)
    return client
