import sys
import glob
import asyncio
import logging
import importlib
import urllib3


from pathlib import Path
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def load_plugins(plugin_name):
    path = Path(f"RAUSHAN/modules/{plugin_name}.py")
    spec = importlib.util.spec_from_file_location(f"RAUSHAN.modules.{plugin_name}", path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["RAUSHAN.modules." + plugin_name] = load
    print("Altron has Imported " + plugin_name)


files = glob.glob("RAUSHAN/modules/*.py")
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("\n𝐀𝐥𝐩𝐡𝐚 𝐒𝐩𝐚𝐦 𝐁𝐨𝐭𝐬 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ⚡\nMy Master ---> @ll_ALPHA_BABY_lll")


async def main():
    clients = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]
    tasks = [client.run_until_disconnected() for client in clients if client.is_connected()]
    if tasks:
        await asyncio.gather(*tasks)
    else:
        print("Warning: No bot clients are currently connected. Please configure BOT_TOKEN in environment variables.")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
