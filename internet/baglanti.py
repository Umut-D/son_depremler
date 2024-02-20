# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name
# pylint: disable=import-error
# pylint: disable=line-too-long
from urllib import request
from urllib.error import URLError
from dosya.tarih import Tarih


class Baglanti:
    def __init__(self):
        tarih = Tarih()
        self.url = f"https://deprem.afad.gov.tr/apiv2/event/filter?&{tarih.son_24_saat()}&format=json"

    def indir(self) -> str | None:
        try:
            with request.urlopen(self.url, timeout=10) as response:
                if response.getcode() == 200:
                    return response.read()
        except URLError:
            return "Web sayfası indirilerken bir veya birkaç hata oldu."

        return None
