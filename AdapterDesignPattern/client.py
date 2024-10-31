from legacycharger import LegacyCharger
from adapter import Adapter
if __name__ == "__main__":
    legacycharger=LegacyCharger()
    adapter=Adapter(legacycharger)
    adapter.charge_via_usb()