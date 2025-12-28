import os
import re


def replace_promt_placeholder(prompt: str) -> str:
    """
    Unitility function to replace {{placeholder}} with %(placeholder)s,
    so prompts can be copy-pasted from Claude Console.
    """
    return re.sub(r"\{\{(\w+)\}\}", r"%(\1)s", prompt)


def load_prompt_template_from_file(file_name: str) -> str:
    template_path = os.path.join(os.path.dirname(__file__), "prompts", file_name)
    with open(template_path, "r", encoding="utf-8") as f:
        return f.read()
