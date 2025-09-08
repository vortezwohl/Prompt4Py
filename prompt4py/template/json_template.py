import json

from prompt4py.template.base_template import BaseTemplate


class JsonTemplate(BaseTemplate):
    def __init__(self):
        super().__init__()

    def render_system(self):
        _prompt_object = {
            'role': self.role,
            'objective': self.objective,
            'constraint': self.constraint,
            'capability': self.capability,
            'output_datatype': self.output_dtype,
            'output_format': self.output_format,
            'output_language': self.output_language,
            'output_example': self.output_example
        }
        for k in list(_prompt_object.keys()):
            if len(str(_prompt_object[k])) < 1:
                del _prompt_object[k]
        return json.dumps(_prompt_object, ensure_ascii=False)

    def render_user(self):
        _prompt_object = {
            'instruction': self.instruction,
            'context': self.context
        }
        for k in list(_prompt_object.keys()):
            if len(str(_prompt_object[k])) < 1:
                del _prompt_object[k]
        return json.dumps(_prompt_object, ensure_ascii=False)

    def render(self) -> str:
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
        return json.dumps(_prompt_object, ensure_ascii=False)
