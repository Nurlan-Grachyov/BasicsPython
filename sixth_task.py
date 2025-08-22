import logging
from datetime import datetime, date

from bs4 import BeautifulSoup

LINK_CLASS = "accordeon-inner__item-title link xls"
HREF_PREFIX = "/upload/reports/oil_xls/oil_xls_"
DATE_FORMAT = "%Y%m%d"

logging.basicConfig(
    filename="any_log.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def parse_page_links(html: str, start_date: date, end_date: date, base_url: str) -> list:
    """
    Парсит ссылки на бюллетени с одной страницы:
    <a class="accordeon-inner__item-title link xls" href="/upload/reports/oil_xls/oil_xls_20240101_test.xls">link1</a>
    """

    # логирование в файл для разрабов, принт в консоль для юзеров

    results = []
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_=LINK_CLASS)

    for link in links:
        href = link.get("href")
        if not href:
            continue

        href = href.split("?")[0]
        if HREF_PREFIX not in href or not href.endswith(".xls"):
            continue

        try:
            date = href.split("oil_xls_")[1][:8]
            format_date = datetime.strptime(date, DATE_FORMAT).date()
            if start_date <= format_date <= end_date:
                href_with_base = href if href.startswith("http") else f"{base_url}{href}"
                results.append((href_with_base, format_date))
            else:
                print(f"Ссылка {href} вне диапазона дат")
        except (IndexError, ValueError) as e:
            logging.error(f"Ошибка: {e}")
            print(f"Не удалось извлечь дату из ссылки {href}: {e}")
        except Exception as e:
            logging.error(f"Неизвестная ошибка: {e}")

    return results
