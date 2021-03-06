from django.core.management.base import BaseCommand, CommandError
from rssfeed.models import Feed
import feedparser
import requests
import logging
import sys
import time
from datetime import datetime


class Command(BaseCommand):
    """
    class for loadfeed command processing.
    """
    help = 'Load feed data into database.'

    def add_arguments(self, parser):
        parser.add_argument('url', nargs='+', type=str)

    def handle(self, *args, **options):
        srcurl = options['url'][0]
        attempts = 5
        timeout = 2.000
        logging.basicConfig(level=logging.INFO)
        while attempts:
            attempts = attempts-1
            try:
                data = requests.get(srcurl, timeout = timeout)
                break
            except requests.exceptions.Timeout as e:
                if(attempts<=0):
                    logging.info("Maximum retry attempts reached....Exiting")
                    sys.exit(1)
                logging.info("Request timeout....waiting to retry")
                time.sleep(4)
                timeout = timeout+timeout
                logging.info("Retrying......")
            except requests.exceptions.HTTPError as e:
                logging.info("Exception: And you get an HTTPError:", e.message)
                sys.exit(1)
            except requests.exceptions.ConnectionError as e:
                logging.info("Exception: These aren't the domains you're looking for/check your connectivity")
                sys.exit(1)

        def chunker(seq, size):
            return (seq[pos:pos + size] for pos in range(0, len(seq), size))
        
        feed = feedparser.parse(data.content)
        guid_list = [item.guid for item in feed['entries']]
        exist_guid = []
        for guid_chunk in chunker(guid_list, 10):
            exist_guid_chunk = [ x.guid for x in Feed.objects.filter(guid__in = guid_chunk)]
            exist_guid.extend(exist_guid_chunk)

        insert_guid = list(set(guid_list) - set(exist_guid))

        for item in feed['entries']:
            if item.guid not in insert_guid:
                continue
            guid = item.guid
            title = item.title
            description = item.summary
            publishdate = str(datetime.strptime(item.published,"%a, %d %b %Y %H:%M:%S %z"))
            url = item.link
            feed_object = Feed(title = title, description = description, publishdate = publishdate, guid = guid, url = url, srcurl = srcurl)
            feed_object.save()

        logging.info("  %d records inserted into database"%len(insert_guid))
