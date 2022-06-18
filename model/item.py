from typing import List
from pydantic import BaseModel

class Item(BaseModel):
  uuid: str
  uri: str
  label: str
  identifier: str
  notation: str
  alt_label: List[str]
  definition: str
