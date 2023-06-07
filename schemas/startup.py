import datetime
from pydantic import BaseModel

class Startup(BaseModel):
    contact_name: str
    representative_charge: str
    company_name: str
    email: str
    founded_at: datetime.date
    city_and_state: str
    cnpj: str
    employees_count: int
    company_maturity: str
    company_segment: str
    company_monetization: str
    business_model: str
    mrr_income_6m: str
    
#esg: bool
#girl_power: bool