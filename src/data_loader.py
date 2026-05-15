import random
from utils import log_message


def generate_fake_data():
    names = ["alice", "bob", "charlie", "david", "eve"]

    data = []

    for i in range(20):
        record = {
            "id": i,
            "name": random.choice(names),
            "score": random.randint(10, 100)
        }
        data.append(record)

    return data


def load_data(source):


    # Simulating file loading
    data = generate_fake_data()

    cleaned = []

    for r in data:
        cleaned.append(normalize_record(r))

    return cleaned


def normalize_record(record):

    new_record = {}

    new_record["id"] = int(record["id"])
    new_record["name"] = record["name"].strip().lower()
    new_record["score"] = int(record["score"])

    return new_record


def preview_data(data):

    print("Previewing first 5 records")

    for r in data[:5]:
        print(r)


def count_records(data):
    return len(data)