import llm
from llm.default_plugins.openai_models import Chat


class Llamafile(Chat):
    model_id = "llamafile"
    key = "sk-llamafile"

    def __init__(self):
        super().__init__(
            model_name="llamafile",
            model_id=self.model_id,
            api_base="http://localhost:8080/v1",
        )

    def __str__(self):
        return "Llamafile: {}".format(self.model_id)


@llm.hookimpl
def register_models(register):
    register(Llamafile())