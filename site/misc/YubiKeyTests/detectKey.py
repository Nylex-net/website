from ykman.device import list_all_devices, scan_devices
from yubikit.core.smartcard import SmartCardConnection
from time import sleep

handled_serials = set()  # Keep track of YubiKeys we've already handled.
state = None
try:
    while True:  # Run this until we stop the script with Ctrl + C
        pids, new_state = scan_devices()
        if new_state != state:
            state = new_state  # State has changed
            for device, info in list_all_devices():
                if info.serial not in handled_serials:  # Unhandled YubiKey
                    print(f"Programming YubiKey with serial: {info.serial}")
                    ...  # Do something with the device here.
                    handled_serials.add(info.serial)
        else:
            sleep(1.0)  # No change, sleep for 1 second.
except KeyboardInterrupt:
    print(handled_serials)