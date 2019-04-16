import json
import os

from datetime import datetime
from urllib.request import urlopen

FILEPATH = "/tmp/runescape.log"


class Item:
    def __init__(self, name, desc, price, delta):
        self.name = name
        self.description = desc
        self.price = price
        self.delta = delta

    @classmethod
    def from_json_data(cls, data):
        item = data["item"]
        return cls(
            item["name"],
            item["description"],
            item["current"]["price"],
            item["today"]["price"],
        )

    def __repr__(self):
        return "\n".join([
            self.name,
            self.description,
            f"Current price: {self.price}",
            f"Change: {self.delta}",
        ])


def notify(title: str, subtitle: str, message: str):
    t = "-title {!r}".format(title)
    s = "-subtitle {!r}".format(subtitle)
    m = "-message {!r}".format(message)
    os.system("/usr/local/bin/terminal-notifier {}".format(" ".join([m, t, s])))


def get_item_by_id(item_id: int) -> Item:
    """
    Given an item id, returns json formatted data about the item and its price
    on the Grand Exchange
    """
    base_url = "http://services.runescape.com/m=itemdb_oldschool/api/" \
        "catalogue/detail.json?item="
    url = base_url + str(item_id)

    response = urlopen(url)
    data = json.loads(response.read())
    return Item.from_json_data(data)


def main():
    notify_ids = [
        9075,  # astral rune
    ]

    for item_id in notify_ids:
        item = get_item_by_id(item_id)
        print(item)
        try:
            size = os.path.getsize(FILEPATH)
            mode = "a" if size < 100000 else "w"
        except os.error:
            mode = "w"
        with open(FILEPATH, mode) as f:
            ts_format = "%Y-%m-%d %H:%M"
            header = f"--------[ {datetime.now().strftime(ts_format)} ]--------"
            f.write(f"{header}\n{item}\n")

    notify(
        "Grand Exchange", "Prices updated", "See /tmp/runescape.log for info"
    )
    os.system("/usr/bin/open /tmp/runescape.log")


if __name__ == "__main__":
    main()
