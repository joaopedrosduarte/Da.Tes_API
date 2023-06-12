import datetime
from pydantic import BaseModel

class Instituicao(BaseModel):
    cnpj: str
    
class InfoContatos(BaseModel):
    email: str
    telefone: str
    tipo_ou_cargo_do_contato: str

class Startup(BaseModel):
    esg: bool
    girl_power: bool
    nome: str
    representante_empresa: str
    fundado_em: datetime.date
    qtd_funcionarios: int
    maturidade_empresa: str
    segmento_empresa: str
    tipo_monetizacao: str
    modelo_negocio: str
    tipo_recurso: str
    cidade: str
    estado: str
    regiao: str
    
class ContatosStartup(BaseModel):
    info_contatos_id: int
    whatsapp: str
    instagram: str
    nome: str
    startup_id: int
    
class Recurso(BaseModel):
    nome: str
    valor_liquido: int
    descricao: str
    tipo: str
    cod_tipo: str
    
class OrgaoFomentador(BaseModel):
    instituicao_id: int
    nome: str
    informacoes_adicionais: str
    
class Edital(BaseModel):
    cronograma: str
    data_insc_final: datetime.date
    data_insc_inicial: datetime.date
    objetivo_curto: str
    objetivo_completo: str
    num_vagas: int
    acompanhamento: bool
    segmento: str
    link_acesso: str
    nome_edital: str
    criterios_elegibilidade: str
    finalizado: bool
    cidade: str
    estado: str
    regiao: str
    orgao_fomentador_id: int
    organizador_id: int
    recurso_id: int
    foto: str
    
class MatchSugestao(BaseModel):
    startup_id: int
    edital_id: int
    feedback: str
    data: datetime.date
    avaliacao_txt: str
    avaliacao_nota: int
    
class ContatoOrgaoFomentador(BaseModel):
    info_contatos_id: int
    orgao_fomentador_id: int
    nome: str
    
    
#esg: bool
#girl_power: bool