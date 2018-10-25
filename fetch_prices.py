import urllib
import json
import os

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('/usr/local/bin/terminal-notifier {}'.format(' '.join([m, t, s])))

def print_item_price(id):
    '''
    Given an item id, prints data about the item
    and its price on the Grand Exchange
    '''
    base_url = 'http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item='
    url = base_url + str(id)
    # Get json object from server
    response = urllib.urlopen(url)
    data = json.loads(response.read())

    # Print header
    print data['item']['name']
    print data['item']['description']

    #Print the current price
    print 'Current price: ' + str(data['item']['current']['price'])

    # Print the price change for today
    print 'Change: ' + str(data['item']['today']['price'])

    print # Newline so multiple entries have a gap

# astral rune
print_item_price(9075)

# cannonball
#print_item_price(2)

notify('Grand Exchange', 'Prices updated', 'See /tmp/runescape.log for info')
os.system('/usr/bin/open /tmp/runescape.log')
