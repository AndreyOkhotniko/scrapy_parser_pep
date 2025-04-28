import csv
from datetime import datetime as dt
from collections import defaultdict

from pep_parse.settings import BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
            status = item.get('status')
            self.status_count[status] += 1
            self.total += 1
            return item

    def close_spider(self, spider):
        time_pattern = dt.now().strftime('%Y-%m-%dT%H-%M-%S')
        path_results = BASE_DIR / f'results/status_summary_{time_pattern}.csv'

        with open(
            path_results,
            'w',
            newline='',
            encoding='utf-8'
        ) as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.status_count.items())
            total = sum(self.status_count.values())
            writer.writerow(['Total', total])
