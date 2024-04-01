# venv/bin/python3 upload-torrent.py /path/to/filename.torrent

import logging
import os
import sys

from dotenv import load_dotenv
from transmission_rpc import Client


if len(sys.argv) == 1:
    print('missing argument: torrentfile')
    print('upload-torrent.py <torrentfile>')
    sys.exit(1)

torrent_filename = sys.argv[1]

logger = logging.getLogger(__name__)
script_dir = sys.path[0]
script_filename = os.path.basename(__file__)
script_basename = os.path.splitext(script_filename)[0]
log_filename = f'{script_basename}.log'
logging.basicConfig(filename=f'{script_dir}/{log_filename}', level=logging.INFO)

logger.info('Loading environment variables from .env')
load_dotenv()

client = Client(
    host=os.getenv('HOST'),
    port=int(os.getenv('PORT')),
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD')
)
with open(torrent_filename, "rb") as f:
    logger.info(f'Adding {torrent_filename} to remote transmission daemon via RPC')
    client.add_torrent(f)
logger.info('Done')

