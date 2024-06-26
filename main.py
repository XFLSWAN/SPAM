## @SHIVANSHDWVS
import sys
import glob
import asyncio
import logging
import importlib.util
import urllib3
from pathlib import Path
from config import X1

# Configure logging
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

# Disable insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def load_plugins(plugin_name):
    path = Path(f"SHUKLA/modules/{plugin_name}.py")
    spec = importlib.util.spec_from_file_location(f"SHUKLA.modules.{plugin_name}", path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules[f"SHUKLA.modules.{plugin_name}"] = load
    print(f"SHASHANK has Imported {plugin_name}")

# Load all plugin modules
files = glob.glob("SHUKLA/modules/*.py")
for name in files:
    with open(name) as file:
        patt = Path(file.name)
        plugin_name = patt.stem
        load_plugins(plugin_name)

print("\nThe Bot Has Been Deployed Successfully. 👻\nMy Master ---> @SHIVANSHDEVS")

async def main():
    await X1.run_until_disconnected()

# Start the asyncio event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
