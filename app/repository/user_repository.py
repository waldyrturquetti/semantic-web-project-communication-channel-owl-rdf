import os

from string import Template
from dotenv import load_dotenv
from SPARQLWrapper import SPARQLWrapper, JSON

load_dotenv()

sparql = SPARQLWrapper(
    os.getenv('APACHE_FUSEKI_URI', "http://localhost:3030/cco/sparql")
)

class UserRepository:
    def __init__(self):
        pass

    @staticmethod
    def execute_query(string_query):
        sparql.setQuery(string_query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        return results["results"]["bindings"]

    def get_actions_count_in_each_time_of_day_by_user(self, user_name):
        query = Template("""
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX cco: <http://www.semanticweb.org/1513mxti/ontologies/2023/11/CCOntology#>
            
            SELECT ?name ?timeOfDay (COUNT(?action) as ?actionCount)
            WHERE {
               ?user rdf:type cco:User .
               ?action rdf:type cco:Actions .
              
               ?user cco:Name ?name .
               ?user cco:PERFORM_ACTION ?action .
               ?action cco:Date_and_Time ?actionDateTime .
               
               # Extracting the hour component
               BIND(HOURS(?actionDateTime) as ?hour) .
            
               # Categorizing actions based on time of day
               BIND(
                  IF(?hour >= 6 && ?hour < 12, "Morning",
                     IF(?hour >= 12 && ?hour < 18, "Afternoon",
                        IF(?hour >= 18 && ?hour < 24, "Evening",
                           IF(?hour >= 0 && ?hour < 6, "Night", "Undefined")
                        )
                     )
                  ) as ?timeOfDay
               )
               FILTER (regex(?name, "$name", "i"))
            }
            GROUP BY ?name ?timeOfDay
        """)
        query = query.substitute(name=user_name)
        return self.execute_query(query)

    def get_actions_count_for_each_action_category_by_user(self, user_name):
        query = Template("""
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX cco: <http://www.semanticweb.org/1513mxti/ontologies/2023/11/CCOntology#>
            
            SELECT ?name ?actionCategory (COUNT(?actionCategory) as ?actionCategoryCount)
            WHERE {
               ?user rdf:type cco:User .
               ?action rdf:type cco:Actions .
              
               ?user cco:Name ?name .
               ?user cco:PERFORM_ACTION ?action .
               ?action cco:Action_Category ?actionCategory .
               
               FILTER (regex(?name, "$name", "i"))
            }
            GROUP BY ?name ?actionCategory
        """)
        query = query.substitute(name=user_name)
        return self.execute_query(query)

    def get_greater_action_count_per_category_by_user(self, user_name):
        query = Template("""
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX cco: <http://www.semanticweb.org/1513mxti/ontologies/2023/11/CCOntology#>
            
            SELECT ?name ?actionCategory ?actionCategoryCount
            WHERE {
              {
                SELECT ?name ?actionCategory (COUNT(?actionCategory) as ?actionCategoryCount)
                WHERE {
                  ?user rdf:type cco:User .
                  ?action rdf:type cco:Actions .
                  ?user cco:Name ?name .
                  ?user cco:PERFORM_ACTION ?action .
                  ?action cco:Action_Category ?actionCategory .
                  FILTER (regex(?name, "$name", "i"))
                }
                GROUP BY ?name ?actionCategory
              }
            
              {
                SELECT ?name (MAX(?actionCategoryCount) as ?maxCount)
                WHERE {
                  {
                    SELECT ?name ?actionCategory (COUNT(?actionCategory) as ?actionCategoryCount)
                    WHERE {
                      ?user rdf:type cco:User .
                      ?action rdf:type cco:Actions .
                      ?user cco:Name ?name .
                      ?user cco:PERFORM_ACTION ?action .
                      ?action cco:Action_Category ?actionCategory .
                      FILTER (regex(?name, "$name", "i"))
                    }
                    GROUP BY ?name ?actionCategory
                  }
                }
                GROUP BY ?name
              }
            
              FILTER (?actionCategoryCount = ?maxCount)
            }
        """)
        query = query.substitute(name=user_name)
        return self.execute_query(query)

    def get_all_comm_resources_and_categories_by_user(self, user_name):
        query = Template("""
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX cco: <http://www.semanticweb.org/1513mxti/ontologies/2023/11/CCOntology#>
            PREFIX cco2: <http://www.semanticweb.org/1513mxti/ontologies/2024/0/CCOntology#>
            
            SELECT ?name ?communication_resource_type ?communication_channel_category_type
            WHERE {
              ?user rdf:type cco:User .
              ?communication_resource rdf:type cco:Communication_Resource .
              ?communication_channel rdf:type cco:Communication_Channel .
            
              ?user cco:Name ?name .
              ?user cco:HAVE ?communication_resource .
              ?communication_resource cco:USE ?communication_channel .
            
              ?communication_resource cco2:Value ?communication_resource_type .
              ?communication_channel cco:Communication_Category ?communication_channel_category_type .
            
              FILTER (?name = "$name"^^xsd:string )
            }
            GROUP BY ?name ?communication_resource_type ?communication_channel_category_type
        """)
        query = query.substitute(name=user_name)
        return self.execute_query(query)

    def get_comm_resources_by_user_and_category(self, user_name, comm_category):
        query = Template("""
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX cco: <http://www.semanticweb.org/1513mxti/ontologies/2023/11/CCOntology#>
            PREFIX cco2: <http://www.semanticweb.org/1513mxti/ontologies/2024/0/CCOntology#>
            
            SELECT ?name ?communication_resource_type ?communication_channel_category_type
            WHERE {
              ?user rdf:type cco:User .
              ?communication_resource rdf:type cco:Communication_Resource .
              ?communication_channel rdf:type cco:Communication_Channel .
            
              ?user cco:Name ?name .
              ?user cco:HAVE ?communication_resource .
              ?communication_resource cco:USE ?communication_channel .
            
              ?communication_resource cco2:Value ?communication_resource_type .
              ?communication_channel cco:Communication_Category ?communication_channel_category_type .
            
              FILTER (?name = "$name"^^xsd:string && ?communication_channel_category_type = "$category"^^xsd:string)
            }
            GROUP BY ?name ?communication_resource_type ?communication_channel_category_type
        """)
        query = query.substitute(name=user_name, category=comm_category)
        return self.execute_query(query)