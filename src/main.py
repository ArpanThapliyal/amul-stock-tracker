import logging
import json
from pathlib import Path

from tracker import is_in_stock
from notifier import send_email

STATE_FILE = Path("state.json") 

Path("logs").mkdir(
    exist_ok=True
)

logging.basicConfig(
    filename="logs/tracker.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def load_state():

    if not STATE_FILE.exists():

        return {
            "last_status": "unknown"
        }

    with open(
        STATE_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def save_state(status):

    with open(
        STATE_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            {
                "last_status": status
            },
            f,
            indent=4
        )


def main():

    state = load_state()

    previous_status = state["last_status"]

    current_status = (
        "in_stock"
        if is_in_stock()
        else "out_of_stock"
    )

    print(
        f"Previous: {previous_status}"
    )

    print(
        f"Current: {current_status}"
    )
    logging.info(
        f"Previous={previous_status}, Current={current_status}"
    )

    if (
        previous_status != "in_stock"
        and current_status == "in_stock"
    ):

        send_email(
            "🚨🚨🚨⚠️⚠️⚠️ Amul Protein Buttermilk In Stock",
            "The product is available. Buy quickly."
        )

        logging.info(
            "Stock alert email sent."
        )

        print(
            "Email sent."
        )

    save_state(current_status)


if __name__ == "__main__":
    main()