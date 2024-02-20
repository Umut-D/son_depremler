# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name
# pylint: disable=import-error
import json


class Depremler:
    def __init__(self, baglanti):
        self._json = baglanti  # Dependecy Injection

    def json_veri(self):
        return json.loads(self._json.indir())

    def json_veriler(self) -> list | str:
        try:
            depremler = []
            for event in self.json_veri():
                if event['magnitude'] != 0:
                    pass

                depremler.append([
                    f"{event['date'].replace('T', ' ')}",
                    f"{event['location']}",
                    f"{event['magnitude']}",
                    f"{event['latitude']}",
                    f"{event['longitude']}",
                    f"{event['depth']}",
                ])

            return sorted(depremler, reverse=True)

        except json.JSONDecodeError:
            return "JSON verisi okunamadı"
