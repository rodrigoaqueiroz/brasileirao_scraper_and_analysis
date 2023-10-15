import scrapy


class CbfSpider(scrapy.Spider):

    name = 'cbf_spider'
    BASE_URL = 'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a'
    start_urls = [BASE_URL]
    ROW_XPATH = '//tr[contains(@class, "expand-trigger")]'
    OLD_ROW_XPATH = '//table[@class="table m-b-20 tabela-expandir"]/tbody/tr'
    GOALS_TABLE = '//table[contains(@class, "table border-body")]/tbody/tr'

    def start_requests(self):
        for year in range(2012, 2024):
            url = f"{self.BASE_URL}/{year}"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        year = response.url.split("/")[-1]
        rows = response.xpath(self.ROW_XPATH)
        if not rows:
            rows = response.xpath(self.OLD_ROW_XPATH)[:20]
        for row in rows:
            data = self.extract_data_from_row(row, year)
            yield data

    def extract_data_from_row(self, row, year):
        return {
            "year": year,
            "position": row.xpath("./td[1]/b/text()").get()[:-1],
            "team": row.xpath('./td[1]/span[contains(@class,"hidden-xs")]/text()').get(),
            "points": row.xpath("./th/text()").get(),
            "games": row.xpath("./td[2]/text()").get(),
            "wins": row.xpath("./td[3]/text()").get(),
            "draws": row.xpath("./td[4]/text()").get(),
            "losses": row.xpath("./td[5]/text()").get(),
            "goals_for": row.xpath("./td[6]/text()").get(),
            "goals_against": row.xpath("./td[7]/text()").get(),
            "goal_difference": row.xpath("./td[8]/text()").get(),
            "percentage": row.xpath("./td[11]/text()").get(),
            "top_player_scorer": {
                "team": row.xpath(f"{self.GOALS_TABLE}/td[1]/img/@title").get(),
                "name": row.xpath(f"{self.GOALS_TABLE}/td[3]/a/text()").get(),
                "goals": row.xpath(f"{self.GOALS_TABLE}/th/text()").get(),
            }
        }
