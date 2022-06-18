from py2neo.ogm import Model, Property, RelatedTo
from neo4j.concept import Concept
from neo4j.neo4j_database import Neo4jDatabase
from model.term import Term

class SkosConcept(Concept):
  identifier = Property()
  notation = Property()
  alt_label = Property()
  pref_label = Property()
  definition = Property()

  narrower = RelatedTo('SkosConcept', "NARROWER")

  @classmethod
  def find_within_parent(cls, parent_identifier, identifier):
    db = Neo4jDatabase()
    query = """
      MATCH (n:SkosConcept)-[:NARROWER]->(m:SkosConcept) WHERE n.identifier='%s' AND m.identifier='%s' RETURN m
    """ % (parent_identifier, identifier)
    results = db.graph().run(query).data()
    return dict(results[0]['m'])

  @classmethod
  def like(cls, term):
    results = []
    db = Neo4jDatabase()
    # query = """
    #   MATCH (n:SkosConcept) WHERE n.pref_label CONTAINS '%s' OR n.definition CONTAINS '%s' OR n.alt_label CONTAINS '%s' RETURN n
    # """ % (term, term, term)
    query = """
      MATCH (n:SKOS_CONCEPT) WHERE n.pref_label CONTAINS '%s' OR n.definition CONTAINS '%s' OR n.alt_label CONTAINS '%s' RETURN n
    """ % (term, term, term)
    print("query",query)
    items = db.graph().run(query).data()
    print("items",items)
    for item in items:
      print("\n  -item",item)
      x = dict(item['n'])
      print("\n  -x)",x)
      results.append(Term(**x))
    print("\n--done---\n",item)
    return results
