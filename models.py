# task and project dataclasses

from dataclasses import dataclass
from typing import Optional

@dataclass
class project:
    id : int
    name :str
    created_ad : str

@dataclass
class task:
    id : int
    project_id : int
    description : str
    is_complete : bool
    due_date : Optional[str]
    created_at : str