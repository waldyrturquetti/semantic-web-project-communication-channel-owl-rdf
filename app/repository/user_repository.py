import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()


class UserRepository:
    def __init__(self):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self.driver.close()