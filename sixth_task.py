import logging
from datetime import datetime, date

from bs4 import BeautifulSoup

logging.basicConfig(
    filename='any_log.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def parse_page_links(html: str, start_date: date, end_date: date, url: str):
    """
    Парсит ссылки на бюллетени с одной страницы:
    <a class="accordeon-inner__item-title link xls" href="/upload/reports/oil_xls/oil_xls_20240101_test.xls">link1</a>
    """
    results = []
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="accordeon-inner__item-title link xls")

    for link in links:
        href = link.get("href")
        if not href:
            continue

        href = href.split("?")[0]
        if "/upload/reports/oil_xls/oil_xls_" not in href or not href.endswith(".xls"):
            continue

        try:
            date = href.split("oil_xls_")[1][:8]
            file = datetime.strptime(date, "%Y%m%d").date()
            if start_date <= file <= end_date:
                u = href if href.startswith("http") else f"https://spimex.com{href}"
                results.append((u, file))
            else:
                print(f"Ссылка {href} вне диапазона дат")
        except (IndexError, ValueError) as e:
            logging.error(f"Ошибка: {e}")
            print(f"Не удалось извлечь дату из ссылки {href}: {e}")
            continue
        except Exception as e:
            logging.error(f"Неизвестная ошибка: {e}")

    return results
