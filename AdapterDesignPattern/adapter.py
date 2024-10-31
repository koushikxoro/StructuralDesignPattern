from usbcharger import USBCharger
from legacycharger import LegacyCharger
class Adapter(USBCharger):
    def __init__(self, legacy_charger:LegacyCharger):
        self.legacy_charger=legacy_charger
    def charge_via_usb(self):
        self.legacy_charger.charge_via_legacy_port()