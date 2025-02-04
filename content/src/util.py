from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from duckduckgo_search import DDGS
from markitdown import MarkItDown
from typing import Any, List, Tuple
from tqdm.notebook import tqdm
import requests

import os
import shutil

# ddgs = DDGS(proxy="tb", timeout=20)
# this requires the TOR browser to be installed and running for a proxy
# should be used if you plan on querying a lot.
# prepare the markdown extractor
md = MarkItDown()


def with_driver(func):
    def wrapper(*args, **kwargs):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        try:
            result = func(driver, *args, **kwargs)
        finally:
            driver.quit()
        return result

    return wrapper


@with_driver
def get_html(driver, url) -> BeautifulSoup:
    driver.get(url)
    time.sleep(1)  # wait for the page to load
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    return soup


def download_pdf(url, filename="downloaded.pdf"):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024
        tqdm_bar = tqdm(
            total=total_size, unit="iB", unit_scale=True, desc="Downloading PDF"
        )

        with open(filename, "wb") as pdf_file:
            for chunk in response.iter_content(chunk_size=block_size):
                pdf_file.write(chunk)
                tqdm_bar.update(len(chunk))

        tqdm_bar.close()

        print(f"PDF downloaded successfully: {filename}")

    except requests.RequestException as e:
        print(f"Error downloading PDF: {e}")


class WebSearch:
    def __init__(self):
        self.ddgs = DDGS(timeout=20)

    def get_urls(self, query: str, max_results: int = 3, locale="us-en") -> List[str]:
        res = self.ddgs.text(
            f"filetype:pdf {query}",
            max_results=max_results,
            region=locale,
            safesearch="on",
        )
        hrefs = [r["href"] for r in res]
        return hrefs


def split_markdown(
    pdf_folder: str = "tmp",
    out_folder: str = "tmp-markdown",
    MAX_RESULTS: int = 100,
) -> None:

    current_pdfs = sorted(os.listdir(pdf_folder))
    tqdm_iterator = tqdm(current_pdfs, desc="Extracting markdown")

    for pdf_id, pdf in enumerate(tqdm_iterator):
        result = md.convert(os.path.join(pdf_folder, pdf))
        # to deal with large contexts, split by headlines
        hashed_results = result.text_content.split("\n#")
        hashed_results = [
            h.strip() for h in hashed_results if len(h.strip().split("\n")) > 1
        ]

        if len(hashed_results) > MAX_RESULTS:
            hashed_results = hashed_results[:MAX_RESULTS]

        os.makedirs(out_folder, exist_ok=True)

        # we store the markdown unique to each URL in the current session:
        for i, hashed_result in enumerate(hashed_results):
            with open(f"{out_folder}/{pdf_id}_{i}.md", "w") as f:
                # remove all lines in the output with 1 character stripped or less
                tmp_out = "\n".join(
                    [
                        line
                        for line in hashed_result.split("\n")
                        if len(line.strip()) > 1
                    ]
                )
                f.write(tmp_out)
