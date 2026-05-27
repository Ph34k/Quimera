import yaml
from pydantic import BaseModel, Field
from typing import List, Dict, Any

class RuleCondition(BaseModel):
    activity_level: str

class PersuasionRule(BaseModel):
    id: str
    description: str
    condition: RuleCondition
    strategy: str

class PersuasionRuleset(BaseModel):
    version: str
    rules: List[PersuasionRule]

def load_and_validate_rules(filepath: str) -> PersuasionRuleset:
    with open(filepath, "r") as f:
        data = yaml.safe_load(f)
    return PersuasionRuleset(**data)
