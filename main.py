from models.index import startupDB
from schemas.startup import Startup
from fastapi import FastAPI
from config.db import con 

app=FastAPI()

# select startups
@app.get('/api/startups')
async def ListStartups():
    data = con.execute(startupDB.select())
    startups = data.fetchall()
    res = []
    for s in startups:
        res.append({
            "company_id": s.company_id,
            "created_at": s.created_at,
            "updated_at": s.updated_at,
            "deleted_at": s.deleted_at,
            "contact_name": s.contact_name,
            "representative_charge": s.representative_charge,
            "company_name": s.company_name,
            "email": s.email,
            "founded_at": s.founded_at,
            "city_and_state": s.city_and_state,
            "cnpj": s.cnpj,
            "employees_count": s.employees_count,
            "company_maturity": s.company_maturity,
            "company_segment": s.company_segment,
            "company_monetization": s.company_monetization,
            "business_model": s.business_model,
            "mrr_income_6m": s.mrr_income_6m,
        })
    
    return {
        "request": True,
        "data": res
    }     

# search by id
@app.get('/api/startups/id/{company_id}')
async def startupById(companyById:int):
    data = con.execute(startupDB.select().where(startupDB.c.company_id == companyById))
    startupsById = data.fetchall()
    res = []
    for s in startupsById:
        res.append({
            "company_id": s.company_id,
            "created_at": s.created_at,
            "updated_at": s.updated_at,
            "deleted_at": s.deleted_at,
            "contact_name": s.contact_name,
            "representative_charge": s.representative_charge,
            "company_name": s.company_name,
            "email": s.email,
            "founded_at": s.founded_at,
            "city_and_state": s.city_and_state,
            "cnpj": s.cnpj,
            "employees_count": s.employees_count,
            "company_maturity": s.company_maturity,
            "company_segment": s.company_segment,
            "company_monetization": s.company_monetization,
            "business_model": s.business_model,
            "mrr_income_6m": s.mrr_income_6m,
        })
    
    return {
        "request": True,
        "data": res
    }     

# search by company_segment
@app.get('/api/startups/company_segment/{company_segment}')
async def startupBySegment(companySegment:str):
    data = con.execute(startupDB.select().where(startupDB.c.company_segment == companySegment))
    startupsBySegment = data.fetchall()
    res = []
    for s in startupsBySegment:
        res.append({
            "company_id": s.company_id,
            "created_at": s.created_at,
            "updated_at": s.updated_at,
            "deleted_at": s.deleted_at,
            "contact_name": s.contact_name,
            "representative_charge": s.representative_charge,
            "company_name": s.company_name,
            "email": s.email,
            "founded_at": s.founded_at,
            "city_and_state": s.city_and_state,
            "cnpj": s.cnpj,
            "employees_count": s.employees_count,
            "company_maturity": s.company_maturity,
            "company_segment": s.company_segment,
            "company_monetization": s.company_monetization,
            "business_model": s.business_model,
            "mrr_income_6m": s.mrr_income_6m,
        })
    
    return {
        "request": True,
        "data": res
    }     

# Create new startup
@app.post('/api/new_startup')
async def newStartup(startup:Startup):
    data=con.execute(startupDB.insert().values(
        contact_name=startup.contact_name,
        representative_charge=startup.representative_charge,
        company_name=startup.company_name,
        email=startup.email,
        founded_at=startup.founded_at,
        city_and_state=startup.city_and_state,
        cnpj=startup.cnpj,
        employees_count=startup.employees_count,
        company_maturity=startup.company_maturity,
        company_segment=startup.company_segment,
        company_monetization=startup.company_monetization,
        business_model=startup.business_model,
        mrr_income_6m=startup.mrr_income_6m,
    ))

    if data.is_insert:
        con.commit()
        return {
            "success": True,
            "msg":"Student Store Successfully"
        }
    else:
         return {
            "success": False,
            "msg":"Some Problem"
        }

# delete data by id
@app.delete('/api/delete_startup/{company_id}')
async def deleteStartup(company_id:int):
    data=con.execute(startupDB.delete().where( startupDB.c.company_id == company_id ))
    if data:
        con.commit()
        return {
            "success": True,
            "msg":"Startup Delete Successfully"
        }
    else:
        return {
            "success": False,
            "msg":"Some Problem"
        }
