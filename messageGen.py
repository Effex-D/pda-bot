from pymongo import MongoClient
from message_queue import messageLoader
import sys
import json

if len(sys.argv) != 2:
    print("This script takes exactly 1 argument.")
    print("Usage: messageGen.py message")
    print("Please try again.")
    exit(1)

with open('config.json') as config_file:
    config = json.load(config_file)
    database_name = config['database_name']

message = sys.argv[1]

ml = messageLoader(database_name)
ml.add_to_queue(message)