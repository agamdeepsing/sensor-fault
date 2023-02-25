import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

data_file = "aps_failure_training_set1.csv"
database_name = "aps"
collection_name = "sensor"


if __name__ == "__main__":
    df = pd.read_csv(data_file)
    print(f"Rows and columns:{df.shape}")


    ##Convert dataframe to json before dropping to mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())

    print(json_record[0])


    #insert json conv record to mongo db
    client[database_name][collection_name].insert_many(json_record)
