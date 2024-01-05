import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

from app.dto.comm_channels_and_comm_resources_dto import serialize_comm_channels_and_comm_resources
from app.dto.actions_by_comm_channel_dto import serialize_action_by_comm_channel
from app.dto.comm_resources_by_comm_channel_dto import serialize_comm_resources_by_comm_channel
from app.dto.users_by_comm_channel_dto import serialize_users_by_comm_channel

load_dotenv()

uri = os.getenv("NEO4J_URI", "bolt://127.0.0.1:7687")
username = os.getenv("NEO4J_USER", "neo4j")
password = os.getenv("NEO4J_PASSWORD", "Str@ngPassword")
database = os.getenv("NEO4J_DATABASE", "neo4j")


class CommChannelRepository:
    def __init__(self):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self.driver.close()

    @staticmethod
    def _get_user_commchannels(tx, name):
        nodes = tx.run(
            "MATCH (u:User {name:$name})-[:HAVE]->(a)-[:USE]->(cc:ChannelCommunication) RETURN collect(distinct cc)",
            name=name)
        results = [record for record in nodes.data()]
        return results[0]['collect(distinct cc)']

    def get_user_commchannels(self, name):
        with self.driver.session() as session:
            commchannel = session.execute_read(self._get_user_commchannels, name)
            self.close()
            return commchannel

    @staticmethod
    def _get_comm_channels_and_comm_resources_by_user(tx, name):
        nodes = tx.run(
            "MATCH path = (u:User {name:$name})-[h:HAVE]->(a)-[*]->(cc:ChannelCommunication)"
            " RETURN u,PROPERTIES(h),a,cc;", name=name)
        return serialize_comm_channels_and_comm_resources(nodes.data())

    def get_comm_channels_and_comm_resources_by_user(self, user_name):
        with self.driver.session() as session:
            comm_channel = session.execute_read(self._get_comm_channels_and_comm_resources_by_user, user_name)
            self.close()
            return comm_channel

    @staticmethod
    def _get_comm_resources_by_comm_channel(tx, cc_type):
        nodes = tx.run(
            "MATCH path = (A)-[:USE]->(cc:ChannelCommunication {type:$cc_type}) RETURN A;", cc_type=cc_type)
        return serialize_comm_resources_by_comm_channel(nodes.data())

    def get_comm_resources_by_comm_channel(self, cc_type):
        with self.driver.session() as session:
            comm_channel = session.execute_read(self._get_comm_resources_by_comm_channel, cc_type)
            self.close()
            return comm_channel

    @staticmethod
    def _get_actions_by_comm_channel(tx, cc_type):
        nodes = tx.run(
            "MATCH path = (a:Action)-[:THROUGH_A]->(cc:ChannelCommunication {type:$cc_type}) RETURN a;", cc_type=cc_type)
        return serialize_action_by_comm_channel(nodes.data())

    def get_actions_by_comm_channel(self, cc_type):
        with self.driver.session() as session:
            comm_channel = session.execute_read(self._get_actions_by_comm_channel, cc_type)
            self.close()
            return comm_channel

    @staticmethod
    def _get_the_best_comm_channels_and_comm_resources_by_user(tx, name):
        nodes = tx.run(
            "MATCH path = (u:User {name:$name})-[h:HAVE]->(a)-[*]->(cc:ChannelCommunication) "
            "WITH max(h.preference_weight) as maxPreference "
            "MATCH path = (user:User {name:$name})-[h:HAVE]->(a)-[*]->(cc:ChannelCommunication) "
            "WHERE h.preference_weight = maxPreference "            
            "RETURN PROPERTIES(h),a,cc;", name=name)
        return serialize_comm_channels_and_comm_resources(nodes.data())

    def get_the_best_comm_channels_and_comm_resources_by_user(self, user_name):
        with self.driver.session() as session:
            comm_channel = session.execute_read(self._get_the_best_comm_channels_and_comm_resources_by_user, user_name)
            self.close()
            return comm_channel

    @staticmethod
    def _get_users_by_comm_channel(tx, cc_type):
        nodes = tx.run(
            "MATCH path = (cc:ChannelCommunication {type:$cc_type})<-[*]-(a)<-[:HAVE]-(u:User) RETURN collect(distinct u);", cc_type=cc_type)
        results = [record for record in nodes.data()]
        return serialize_users_by_comm_channel(results[0]['collect(distinct u)'])

    def get_users_by_comm_channel(self, cc_type):
        with self.driver.session() as session:
            comm_channel = session.execute_read(self._get_users_by_comm_channel, cc_type)
            self.close()
            return comm_channel
