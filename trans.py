import asyncio
import sys

from googletrans import Translator


async def translate(*argv):
    async with Translator() as translator:
        results = await translator.translate(
            text=" ".join(argv[0][1:]), dest="hu", source="en"
        )
    if results.text:
        print(results.text)


asyncio.run(translate(sys.argv))
