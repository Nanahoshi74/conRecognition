from icrawler.builtin import BingImageCrawler

coin_list=['一円玉', '五円玉', '十円玉', '五十円玉', '百円玉', '五百円玉', '小銭 画像']

#スクレイピングを行う関数
def scraping(word, max_num, path):
    bing_crawler = BingImageCrawler(downloader_threads = 4, storage = {'root_dir': path})
    bing_crawler.crawl(keyword = word, filters = None, offset = 0, max_num = max_num,
                       min_size=(200, 200), max_size = None)
# スクレイピング実行
for i in range(len(coin_list)):
    scraping(coin_list[i], 200, './coin/' + coin_list[i] + '/')
