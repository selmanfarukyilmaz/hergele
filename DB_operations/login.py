import pymongo
from pymongo import MongoClient
from omegaconf import OmegaConf

conf = OmegaConf.load(f'../config.yaml')

uri = f"mongodb+srv://{conf['username']}:{conf['password']}@hergele.himq714." \
      "mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

db = client[conf["db_name"]]

