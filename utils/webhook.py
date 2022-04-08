from discord_webhook import DiscordWebhook


def send_message(webhook_url, puzzle_number, link):
    print(f'New link: Puzzle {puzzle_number} - {link}, sending to webhook...')
    content = f'#{puzzle_number} - {link}'
    webhook = DiscordWebhook(
        url=webhook_url,content=content, rate_limit_retry=True
        )
    webhook.execute()

