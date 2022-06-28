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
  def get_bcs(cls):
    db = Neo4jDatabase()
    query = f"""MATCH (bc:BC_INSTANCE) RETURN * limit 10"""
    print("query",query)
    results = db.graph().run(query)
    return results

  @classmethod
  def get_bc_items(cls, bc):
    db = Neo4jDatabase()
    # query = f"""MATCH (bc:BC_INSTANCE)-[:HAS_ITEM]->(item) RETURN * limit 2"""
    query = f"""
MATCH (bc:BC_INSTANCE)-[:HAS_ITEM]->(item)
where bc.name = "{bc}"
RETURN item limit 10
    """
    print("query",query)
    results = db.graph().run(query)
    return results
