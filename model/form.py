from typing import List
from pydantic import BaseModel

class Form(BaseModel):
  uuid: str
  uri: str
  label: str
  alt_label: List[str]
  pref_label: str
  definition: str
