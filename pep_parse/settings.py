from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
OUTPUT_DIR = 'results'

BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
ROBOTSTXT_OBEY = True
FEEDS = {
    f'{OUTPUT_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
FEED_EXPORT_ENCODING = 'utf-8'
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
