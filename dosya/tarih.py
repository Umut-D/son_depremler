# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name
from datetime import datetime, timedelta


class Tarih:
    def son_24_saat(self) -> str:
        bitis = datetime.today()
        baslangic = bitis - timedelta(days=1)

        bitis = self._donustur(bitis)
        baslangic = self._donustur(baslangic)

        return f"start={baslangic}&end={bitis}"

    @staticmethod
    def _donustur(zaman):
        return f"{zaman.strftime("%x").replace("/", "-")}%20{zaman.strftime("%X")}"
