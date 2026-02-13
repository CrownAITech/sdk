from models.base_model import BaseModel

class CrownModel(BaseModel):
    def predict(self, input_text: str) -> str:
        return f"Crown AI Response to: {input_text}"
