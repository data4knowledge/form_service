from fastapi import FastAPI
from model.system import SystemOut
from model.term import Term
from neo4j.neo4j_database import Neo4jDatabase
from neo4j.skos_concept import SkosConcept
from fastapi_pagination import Page, add_pagination, paginate
from neo4j.form import FormThingy
import json

VERSION = "0.1"
SYSTEM_NAME = "d4k Form Microservice"

app = FastAPI(
  title = SYSTEM_NAME,
  description = "A microservice to handle brilliant CT in a Neo4j database.",
  version = VERSION
)

@app.get("/",
  summary="Get system and version",
  description="Returns the microservice system details and the version running.", 
  response_model=SystemOut)
async def read_root():
  #return { 'system_name': SYSTEM_NAME, 'version': VERSION }
  # results = SkosConcept.find_bc()
  return SystemOut(**{ 'system_name': SYSTEM_NAME, 'version': VERSION })

@app.get("/skos_concepts/")
async def ct_term(parent: str, item: str):
  return SkosConcept.find_within_parent(parent, item)

@app.get("/skos_concepts/like", response_model=Page[Term])
async def ct_like(text: str):
  return paginate(SkosConcept.like(text))


@app.get("/bc/")
async def bc_search():
  # return {'status': "This works"}
  results = FormThingy.find_bc()
  print("type(results)",type(results))
  # return {'status': "You wanted %s" % (results)}
  # json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4)
  return {'text': str(results)}

add_pagination(app)
