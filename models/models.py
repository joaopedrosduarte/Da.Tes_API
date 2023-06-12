from sqlalchemy.sql.sqltypes import Integer, String, BigInteger, DateTime, Date, Boolean
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import relationship
from config.db import meta
from datetime import datetime 

instituicaoDB = Table(
    'instituicao', meta,
    Column('id', Integer, primary_key=True, nullable=False, autoincrement=True, index=True),
    Column('cnpj', String(255), nullable=False),
    Column('created_at', DateTime, default=datetime.now(),nullable=False),
    Column('updated_at', DateTime, default=datetime.now(), nullable=False),
    Column('deleted_at', DateTime, nullable=True),
)

infoContatosDB = Table(
    'info_contatos', meta,
    Column('id', Integer, primary_key=True, nullable=False, autoincrement=True, index=True),
    Column('email', String(255), nullable=True),
    Column('telefone', String(255), nullable=True),
    Column('tipo_ou_cargo_do_contato', String(255), nullable=True),
    Column('created_at', DateTime, default=datetime.now(),nullable=False),
    Column('updated_at', DateTime, default=datetime.now(), nullable=False),
    Column('deleted_at', DateTime, nullable=True),
)

startupDB = Table(
    'startup', meta,
    Column('instituicao_id',Integer, ForeignKey('instituicao.id'), nullable=False),
    Column('esg', Boolean, nullable=False, default=0),
    Column('girl_power', Boolean, nullable=False, default=0),
    Column('nome', String(255), nullable=False),
    Column('representante_empresa', String(255), nullable=False),
    Column('fundado_em', Date, nullable=False),
    Column('qtd_funcionarios', Integer, nullable=False),
    Column('maturidade_empresa', String(255), nullable=False),
    Column('segmento_empresa', String(255), nullable=False),
    Column('tipo_monetizacao', String(255), nullable=False),
    Column('modelo_negocio', String(255), nullable=False),
    Column('tipo_recurso', String(255), nullable=False),
    Column('cidade', String(255), nullable=False),
    Column('estado', String(255), nullable=False),
    Column('regiao', String(255), nullable=False),
)

contatosStartupDB = Table(
    'contatos_startup', meta,
    Column('info_contatos_id', Integer, ForeignKey('info_contatos.id'), nullable=False),
    Column('whatsapp', String(255), nullable=True),
    Column('instagram', String(255), nullable=True),
    Column('nome', String(255), nullable=False),
    Column('startup_id', Integer, ForeignKey('startup.instituicao_id'), nullable=False),
    
)

recursoDB = Table(
    'recurso', meta,
    Column('id', Integer, primary_key=True, nullable=False, autoincrement=True, index=True),
    Column('nome', String(255), nullable=False),
    Column('valor_liquido', BigInteger, nullable=False),
    Column('descricao', String(255), nullable=False),
    Column('tipo', String(255), nullable=False),
    Column('cod_tipo', String(255), nullable=False),
    Column('created_at', DateTime, default=datetime.now(),nullable=False),
    Column('updated_at', DateTime, default=datetime.now(), nullable=False),
    Column('deleted_at', DateTime, nullable=True),
)

orgaoFomentadorDB = Table(
    'orgao_fomentador', meta,
    Column('instituicao_id', Integer, ForeignKey('instituicao.id'), nullable=False),
    Column('nome', String(255), nullable=False),
    Column('informacoes_adicionais', String(255), nullable=False),
    
)

editalDB = Table(
    'edital', meta,
    Column('id', Integer, primary_key=True, nullable=False, autoincrement=True, index=True),
    Column('cronograma', String(255), nullable=False),
    Column('data_insc_final', Date, nullable=False),
    Column('data_insc_inicial', Date, nullable=False),
    Column('objetivo_curto', String(255), nullable=False),
    Column('objetivo_completo', String(255), nullable=False),
    Column('num_vagas', Integer, nullable=False),
    Column('acompanhamento', Boolean, nullable=False, default=0),
    Column('segmento', String(255), nullable=False),
    Column('link_acesso', String(255), nullable=False),
    Column('nome_edital', String(255), nullable=False),
    Column('criterios_eligibilidade', String(255), nullable=False),
    Column('finalizado', Boolean, nullable=False, default=0),
    Column('cidade', String(255), nullable=False),
    Column('estado', String(255), nullable=False),
    Column('regiao', String(255), nullable=False),
    Column('orgao_fomentador_id', Integer, ForeignKey('orgao_fomentador.instituicao_id'), nullable=True),
    Column('organizador_id', Integer, ForeignKey('edital.id'), nullable=True),
    Column('recurso_id', Integer, ForeignKey('recurso.id'), nullable=False),
    Column('foto', String(255), nullable=True),
)

matchSugestaoDB = Table(
    'match_sugestao', meta,
    Column('startup_id', Integer, ForeignKey('startup.instituicao_id'), nullable=False),
    Column('edital_id', Integer, ForeignKey('edital.id'), nullable=False),
    Column('feedback', String(255), nullable=False),
    Column('data', DateTime, default=datetime.now(),nullable=False),
    Column('avaliacao_txt', String(255), nullable=False),
    Column('avaliacao_nota', Integer, nullable=False),
)

contatoOrgaoFomentadorDB = Table(
    'contato_orgao_fomentador', meta,
    Column('info_contatos_id', Integer, ForeignKey('info_contatos.id'), nullable=False),
    Column('orgao_fomentador_id', Integer, ForeignKey('orgao_fomentador.instituicao_id'), nullable=False),
    Column('nome', String(255), nullable=False),
)
