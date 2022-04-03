
from dotenv import load_dotenv
import sys
from src.crawler import Crawler


def main():
    crawler = Crawler()
    crawler.scrap()


if __name__ == "__main__":
    load_dotenv()
    sys.exit(main())
