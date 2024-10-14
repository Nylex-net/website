from ykman.device import list_all_devices
from yubikit.core.smartcard import SmartCardConnection

for device, info in list_all_devices():
    if info.version >= (5, 0, 0):  # The info object provides details about the YubiKey
        print(f"Found YubiKey with serial number: {info.serial}")