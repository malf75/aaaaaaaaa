from pydantic import BaseModel

class ListaProjetos(BaseModel):
    name: str

class NovoFuncionario(BaseModel):
    name: str
    sex: str
    role: str
    salary: int
    country: str
    projects: list[ListaProjetos]