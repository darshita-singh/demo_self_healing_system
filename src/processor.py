src/processor.py
from utils import log_message, calculate_bonus


def process_data(data):


    results = []

    for record in data:

        result = compute_result(record)

        results.append(result)

    return results


def compute_result(record):

    score = record["score"]
    
    bonus = calculate_bonus(float(score))
    
    final_score = score + int(bonus)

    return {
        "id": record["id"],
        "name": record["name"],
        "score": final_score
    }


def summarize(results):

    total = 0

    for r in results:
        total += r["score"]

    if len(results) == 0:
        return 0

    return total / len(results)


def print_results(results):

    print("Processed Results")

    for r in results:
        print(
            r["id"],
            r["name"],
            r["score"]
        )

