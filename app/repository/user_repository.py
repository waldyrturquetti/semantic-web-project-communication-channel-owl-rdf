import os

from dotenv import load_dotenv
from neo4j import GraphDatabase
from app.model.user_entity import serialize_user
from app.dto.user_contacts_relationships_dto import serialize_user_contacts_relationship

load_dotenv()

uri = os.getenv("NEO4J_URI", "bolt://127.0.0.1:7687")
username = os.getenv("NEO4J_USER", "neo4j")
password = os.getenv("NEO4J_PASSWORD", "Str@ngPassword")
database = os.getenv("NEO4J_DATABASE", "neo4j")

class UserRepository:
    def __init__(self):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self.driver.close()

    @staticmethod
    def _get_user_by_name(tx, name):
        nodes = tx.run("MATCH (x:User) WHERE x.name = $name RETURN x", name=name)
        results = [record for record in nodes.data()]
        return serialize_user(results[0]['x'])

    def get_user_by_name(self, name):
        with self.driver.session() as session:
            user = session.execute_read(self._get_user_by_name, name)
            self.close()
            return user

    @staticmethod
    def _get_user_contacts_by_user(tx, name):
        nodes = tx.run(
            "MATCH (u:User {name:$name})-[r]-(c:Contact) RETURN u,r,c;", name=name)
        return serialize_user_contacts_relationship(nodes.data())

    def get_user_contacts_by_user(self, name):
        with self.driver.session() as session:
            user_contacts = session.execute_read(self._get_user_contacts_by_user, name)
            self.close()
            return user_contacts