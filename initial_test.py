import asyncio
from crawl4ai import AsyncWebCrawler

BASE_URL = "https://www.seek.com.au/job/83035215"

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(BASE_URL)
        print(result.markdown[:4000])

if __name__ == "__main__":
    asyncio.run(main())
