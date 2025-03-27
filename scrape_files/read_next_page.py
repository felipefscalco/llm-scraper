import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

BASE_URL = "https://www.seek.com.au/jobs?daterange=1&sortmode=ListedDate"

async def main():
    js_commands = [
        "document.querySelector('a[title=\"Next\"]')?.click();"  
    ]
    config = CrawlerRunConfig(js_code=js_commands)

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=BASE_URL,
            config=config
        )
      
    with open("result.txt", "w", encoding="utf-8") as file:
      file.write(str(result))
    
    # Inspect the type and properties of the result
    print(f"Type of result: {type(result)}")
    print(f"Properties and methods of result: {dir(result)}")

if __name__ == "__main__":
    asyncio.run(main())