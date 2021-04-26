from typing import Optional, Pattern

from pydantic import BaseModel, AnyHttpUrl


class MonitorConfigModel(BaseModel):
    web_site: AnyHttpUrl
    period: int
    pattern: Optional[Pattern]
