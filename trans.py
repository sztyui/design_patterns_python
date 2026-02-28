import asyncio

import click
from googletrans import Translator


class TranslatorApi:
    def __init__(self, from_lang: str, to_lang: str) -> None:
        self.from_lang = from_lang
        self.to_lang = to_lang

    async def translate(self, text: str) -> str:
        async with Translator() as translator:
            results = await translator.translate(
                text=" ".join(text), dest=self.to_lang, source=self.from_lang
            )
        return results.text


@click.command()
@click.option("--from", "from_lang", required=True, default="en")
@click.option("--to", "to_lang", required=True, default="hu")
@click.argument("text", nargs=-1, type=click.UNPROCESSED)
def main(from_lang, to_lang, text):
    t = TranslatorApi(from_lang, to_lang)
    result_text: str = asyncio.run(t.translate(text))
    print(result_text)


if __name__ == "__main__":
    main()
