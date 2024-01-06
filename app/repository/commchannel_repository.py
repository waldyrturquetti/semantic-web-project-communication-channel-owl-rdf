import os

from string import Template
from dotenv import load_dotenv
from SPARQLWrapper import SPARQLWrapper, JSON

load_dotenv()

sparql = SPARQLWrapper(
    os.getenv('APACHE_FUSEKI_URI', "http://localhost:3030/cco/sparql")
)


class CommChannelRepository:

    def __init__(self):
        pass

    @staticmethod
    def execute_query(string_query):
        sparql.setQuery(string_query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        return results["results"]["bindings"]

    def get_the_best_comm_channels_and_comm_resources_by_user(self, user_name):
        query = Template("""
            PREFIX owl: <http://www.w3.org/2002/07/owl#> 
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
            PREFIX cco: <http://www.semanticweb.org/1513mxti/ontologies/2023/11/CCOntology#> 
            
            SELECT ?user ?communication_resource ?communication_channel ?preference_weight
            WHERE { 
                ?user rdf:type cco:User; 
                    cco:Name ?user_name .
                ?communication_resource rdf:type cco:Communication_Resource;
                 cco:Preference_Weight ?preference_weight .
                ?user cco:HAVE ?communication_resource .
                {
                    SELECT (MAX(?preference_weight) AS ?max_preference) 
                    WHERE {
                    ?user rdf:type cco:User; 
                        cco:Name "$name"^^xsd:string ; 
                            cco:HAVE ?communication_resource . 
                    ?communication_resource rdf:type cco:Communication_Resource;
                        cco:Preference_Weight ?preference_weight .
                    }
                } 
                ?communication_resource cco:USE ?communication_channel .
                FILTER (?user_name = "$name"^^xsd:string && ?preference_weight = ?max_preference)
            } 
            ORDER BY DESC (?preference_weight)
        """)
        query = query.substitute(name=user_name)
        return self.execute_query(query)