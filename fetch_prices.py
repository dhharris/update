import json
import os

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


# astral rune
item = get_item_by_id(9075)
with open(FILEPATH, "a") as f:
    f.write(str(item))


notify("Grand Exchange", "Prices updated", "See /tmp/runescape.log for info")
os.system("/usr/bin/open /tmp/runescape.log")
