from pydantic import BaseModel


class AppParams(BaseModel):
  width: int | None 
  height: int | None
  title: str | None 
  bg: str | None