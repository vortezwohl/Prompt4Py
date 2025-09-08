import json

from prompt4py.template.base_template import BaseTemplate
from prompt4py.util.json2markdown import json_to_markdown


class GeneralTemplate(BaseTemplate):
    def __init__(self):
        super().__init__()

    def render(self, parse_markdown: bool = False) -> str:
        _prompt_object = {
            'role': self.role,
            'objective': self.objective,
            'instruction': self.instruction,
            'constraint': self.constraint,
            'capability': self.capability,
            'context': self.context,
            'output_datatype': self.output_dtype,
            'output_format': self.output_format,
            'output_language': self.output_language,
            'output_example': self.output_example
        }
        for k in list(_prompt_object.keys()):
            if len(str(_prompt_object[k])) < 1:
                del _prompt_object[k]
        if parse_markdown:
            return json_to_markdown(json_data=_prompt_object)
        return json.dumps(_prompt_object, ensure_ascii=False)
