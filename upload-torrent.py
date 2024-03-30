#!/home/byron/src/transmission-rpc-uploader/venv/bin/python3
#
# venv/bin/python3 upload-torrent.py /path/to/filename.torrent

import os
import sys

from dotenv import load_dotenv
from transmission_rpc import Client


if len(sys.argv) == 1:
    print('missing argument: torrentfile')
    print('upload-torrent.py <torrentfile>')
    sys.exit(1)

torrent_filename = sys.argv[1]

load_dotenv()

client = Client(host=os.getenv('HOST'), port=int(os.getenv('PORT')), username=os.getenv('USERNAME'), password=os.getenv('PASSWORD'))
with open(torrent_filename, "rb") as f:
    client.add_torrent(f)

