from py2neo.ogm import Model, Property, RelatedTo
from neo4j.concept import Concept
from neo4j.neo4j_database import Neo4jDatabase
import json

class FormThingy(Concept):
  identifier = Property()
  notation = Property()
  alt_label = Property()
  pref_label = Property()
  definition = Property()

  # narrower = RelatedTo('SkosConcept', "NARROWER")

  @classmethod
  def find_bc(cls):
    db = Neo4jDatabase()
    # query = """
    #   MATCH (n) RETURN n limit 2
    # """ % (parent_identifier, identifier)
    query = f"""MATCH (n:SKOS_CONCEPT) RETURN n limit 2"""
    print("query",query)
    results = db.graph().run(query)
    # print("results",results)
    # return json.loads(results)
    return results
