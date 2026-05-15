from utils import log_message



def validate_data(data):


    valid = []

    for record in data:

        if not is_valid_id(record):
            continue

        if not is_valid_name(record):
            continue

        if not is_valid_score(record):
            continue

        valid.append(record)

    return valid


def is_valid_id(record):

    if record["id"] < 0:
        return False

    return True


def is_valid_name(record):

    name = record["name"]

    if not name:
        return False

    if len(name) < 3:
        return False

    return True


def is_valid_score(record):

    score = record["score"]
    try:
        score = float(score)
    except (ValueError, TypeError):
        return False
    if score < 0:
        return False
    if score > 100:
        return False
    return True