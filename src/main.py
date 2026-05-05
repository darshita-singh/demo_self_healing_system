import traceback

from data_loader import load_data
from data_validator import validate_data
from processor import process_data
from utils import log_message


def run_pipeline():


    data = load_data("data.txt")

    valid_data = validate_data(data)

    results = process_data(valid_data)

    for r in results:
        print("Processed:", r)



def main():

    try:
        run_pipeline()

    except Exception as e:

        print("\nPipeline crashed!\n")

        traceback.print_exc()   # <-- this prints the full stack trace


if __name__ == "__main__":
    main()