from os import path
from json import dump
from utils import scrape, store, webhook

# input your channel webhook URL - Edit channel > integrations > webhook > New webhook
WEBHOOK_URL = 'https://discord.com/api/webhooks/961835080819544064/i5pfYcxV1-hbV4vzPbgNjVFDacdFUQxK97N0OUlKMtqHNSa7-rwf-CLQ2NigpGNAhQUm'

def check_create_json():
    '''check for history.json, if not exists create'''
    print('Script started, checking for history.json...')

    if not path.exists('./history.json'):
        print('history.json not found, creating...')
        with open('./history.json', 'w') as f:
            dump({}, f)
    else:
        print('history.json was found, moving on...')



def main():
    '''main script'''

    print('Beginning scrape on target URL...')
    puzzle_number, link = scrape.scrape_site()

    print('Scrape successful, checking stored link...')
    old_data = store.load_json()

    if not old_data:
        print('No link found, storing scraped link...')

        old_data[link] = puzzle_number

        store.update_json(old_data)

        print('history.json updated with scraped link and puzzle number, exiting...')
        exit()

    print('Comparing stored link with scraped link...')

    for k, v in old_data.items():

        if k == link:

            print('Links are the same, exiting...')
            exit()

        else:
            # send new link and puzle number to webhook
            webhook.send_message(WEBHOOK_URL, puzzle_number, link)

            # update json with new scraped link
            old_data[link] = puzzle_number
            store.update_json(old_data)


if __name__ == '__main__':
    check_create_json()
    main()