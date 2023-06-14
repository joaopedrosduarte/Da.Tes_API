from models.index import instituicaoDB,editalDB,startupDB
from schemas.schemas import Startup, Instituicao
from fastapi import FastAPI
from config.db import con 

app=FastAPI()

# test conection
@app.get('/')
async def index():
    return { "conection": "success" }

# select editais
@app.get('/api/editais')
async def ListEdital():
    data = con.execute(editalDB.select())
    editais = data.fetchall()
    res = []
    
    for e in editais:
        res.append({
            "id": e.id,
            "cronograma": e.cronograma,
            "data_insc_final": e.data_insc_final,
            "data_insc_inicial": e.data_insc_inicial,
            "objetivo_curto": e.objetivo_curto,
            "objetivo_completo": e.objetivo_completo,
            "num_vagas": e.num_vagas,
            "acompanhamento": e.acompanhamento,
            "segmento": e.segmento,
            "link_acesso": e.link_acesso,
            "nome_edital": e.nome_edital,
            "criterios_eligibilidade": e.criterios_eligibilidade,
            "finalizado": e.finalizado,
            "cidade": e.cidade,
            "estado": e.estado,
            "regiao": e.regiao,
            "orgao_fomentador_id": e.orgao_fomentador_id,
            "organizador_id": e.organizador_id,
            "recurso_id": e.recurso_id,
            "foto": e.foto
        })
    
    return {
        "request": True,
        "data": res
    }     

# select startups
@app.get('/api/startups')
async def ListStartups():
    data = con.execute(startupDB.select())
    startups = data.fetchall()
    res = []
    
    for s in startups:
        res.append({
            "instituicao_id": s.instituicao_id,
            "esg": s.esg,
            "girl_power": s.girl_power,
            "nome": s.nome,
            "representante_empresa": s.representante_empresa,
            "fundado_em": s.fundado_em,
            "qtd_funcionarios": s.qtd_funcionarios,
            "maturidade_empresa": s.maturidade_empresa,
            "segmento_empresa": s.segmento_empresa,
            "tipo_monetizacao": s.tipo_monetizacao,
            "modelo_negocio": s.modelo_negocio,
            "tipo_recurso": s.tipo_recurso,
            "cidade": s.cidade,
            "estado": s.estado,
            "regiao": s.regiao,
        })
    
    return {
        "request": True,
        "data": res
    }     

# Create new startup
@app.post('/api/new_startup')
async def newStartup(instituicao:Instituicao, startup:Startup):
    data=con.execute(instituicaoDB.insert().values(
        cnpj=instituicao.cnpj,
    ))
    
    instKey = data.inserted_primary_key
    if data.is_insert:
        data = con.execute(startupDB.insert().values(
            instituicao_id = instKey[0],
            esg = startup.esg,
            girl_power = startup.girl_power,
            nome = startup.nome,
            representante_empresa = startup.representante_empresa,
            fundado_em = startup.fundado_em,
            qtd_funcionarios = startup.qtd_funcionarios,
            maturidade_empresa = startup.maturidade_empresa,
            segmento_empresa = startup.segmento_empresa,
            tipo_monetizacao = startup.tipo_monetizacao,
            tipo_recurso = startup.tipo_recurso,
            cidade = startup.cidade,
            estado = startup.estado,
            regiao = startup.regiao,
        ))
        if data.is_insert:
            con.commit()
            return {
                "success": True,
                "startup_id": instKey[0]
            }
        else :
            con.rollback()
            return {
            "success": False,
            "msg":"Some problem with the creation of the startup"
            }
            
    else:
        con.rollback()
        return {
            "success": False,
            "msg":"Some problem with the creation of the instituicao"
        }
         
# search by id
# @app.get('/api/startups/id/{company_id}')
# async def startupById(companyById:int):
#     data = con.execute(startupDB.select().where(startupDB.c.company_id == companyById))
#     startupsById = data.fetchall()
#     res = []
    # for s in startupsById:
    #     res.append({
    #         "company_id": s.company_id,
    #         "created_at": s.created_at,
    #         "updated_at": s.updated_at,
    #         "deleted_at": s.deleted_at,
    #         "contact_name": s.contact_name,
    #         "representative_charge": s.representative_charge,
    #         "company_name": s.company_name,
    #         "email": s.email,
    #         "founded_at": s.founded_at,
    #         "city_and_state": s.city_and_state,
    #         "cnpj": s.cnpj,
    #         "employees_count": s.employees_count,
    #         "company_maturity": s.company_maturity,
    #         "company_segment": s.company_segment,
    #         "company_monetization": s.company_monetization,
    #         "business_model": s.business_model,
    #         "mrr_income_6m": s.mrr_income_6m,
    #     })
    
    # return {
    #     "request": True,
    #     "data": res
    # }     

# search by company_segment
# @app.get('/api/startups/company_segment/{company_segment}')
# async def startupBySegment(companySegment:str):
#     data = con.execute(startupDB.select().where(startupDB.c.company_segment == companySegment))
#     startupsBySegment = data.fetchall()
#     res = []
    # for s in startupsBySegment:
    #     res.append({
    #         "company_id": s.company_id,
    #         "created_at": s.created_at,
    #         "updated_at": s.updated_at,
    #         "deleted_at": s.deleted_at,
    #         "contact_name": s.contact_name,
    #         "representative_charge": s.representative_charge,
    #         "company_name": s.company_name,
    #         "email": s.email,
    #         "founded_at": s.founded_at,
    #         "city_and_state": s.city_and_state,
    #         "cnpj": s.cnpj,
    #         "employees_count": s.employees_count,
    #         "company_maturity": s.company_maturity,
    #         "company_segment": s.company_segment,
    #         "company_monetization": s.company_monetization,
    #         "business_model": s.business_model,
    #         "mrr_income_6m": s.mrr_income_6m,
    #     })
    
    # return {
    #     "request": True,
    #     "data": res
    # }     

# # delete data by id
# @app.delete('/api/delete_startup/{company_id}')
# async def deleteStartup(company_id:int):
#     data=con.execute(startupDB.delete().where( startupDB.c.company_id == company_id ))
#     if data:
#         con.commit()
#         return {
#             "success": True,
#             "msg":"Startup Delete Successfully"
#         }
#     else:
#         return {
#             "success": False,
#             "msg":"Some Problem"
#         }
