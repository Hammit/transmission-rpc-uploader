# venv/bin/python3 upload-torrent.py /path/to/filename.torrent

import argparse
import logging
import os
import pathlib

from dotenv import load_dotenv
from transmission_rpc import Client


DEFAULT_TRANSMISSION_PORT = 9091


# Process command-line args
parser = argparse.ArgumentParser(description='Upload a torrent file to a remote Transmission daemon via RPC')
parser.add_argument('torrentfile', type=str, help='the torrent file to upload')
args = parser.parse_args()

torrent_filename = args.torrentfile

# Setup logging
logger = logging.getLogger(__name__)
script_path = pathlib.Path(__file__).resolve()
script_dir = script_path.parent
script_basename = script_path.stem
log_filename = f'{script_basename}.log'
logging.basicConfig(filename=script_path / log_filename, level=logging.INFO)

# Load config/secrets
logger.info('Loading environment variables from .env')
load_dotenv()

# Create the Transmission Client that does the RPC
client = Client(
    host=os.getenv('HOST', ''),
    port=int(os.getenv('PORT', DEFAULT_TRANSMISSION_PORT)),
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD')
)
# Send the torrent
with open(torrent_filename, "rb") as f:
    logger.info(f'Adding {torrent_filename} to remote transmission daemon via RPC')
    client.add_torrent(f)
logger.info('Done')

