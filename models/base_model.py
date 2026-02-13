class BaseModel:
    def predict(self, input_text: str) -> str:
        raise NotImplementedError
