from ykman.device import list_all_devices
from yubikit.core.smartcard import SmartCardConnection
from yubikit.piv import PivSession

# Select a connected YubiKeyDevice
dev, info = list_all_devices()[0]

# Connect to a YubiKey over a SmartCardConnection, which is needed for PIV.
with dev.open_connection(SmartCardConnection) as connection:
    # The connection will be automatically closed after this block

    piv = PivSession(connection)
    attempts = piv.get_pin_attempts()
    print(f"You have {attempts} PIN attempts left.")