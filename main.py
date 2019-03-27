import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()
    text = 'text'
    await page.goto('https://translate.google.com/?hl=zh-CN#view=home&op=translate&sl=en&tl=zh-CN&text=%s' % text)
    await page.addScriptTag(url= 'https://code.jquery.com/jquery-3.3.1.min.js')
    prev_before = None
    while(True):
        before = input()
        if prev_before==before:
            before+="."
        await page.click('.clear-wrap')
        await page.type('.text-dummy',before)
        await page.waitForSelector('span[title]');
        after = await page.evaluate("""(before) =>{
            return $('span[title]').text();
        }
        
        """)
        prev_before = before
        print(after)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
