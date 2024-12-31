# Torrent Uploader for Transmission Daemon


## Overview

This script can be used to upload a local torrent file to a remote Transmission daemon via RPC.
The configuration is via a `.env` file, the template for which can be found in `env.template`.
The reason you would normally use this script is part of a setup where torrents are auto-downloaded
locally and upon local download, uploaded to the remote Transmission daemon, probably running on a
Raspberry Pi operating as a seedbox.


## Installation

* Create virtualenv: `virtualenv -p python3 venv`
* Install dependencies: `venv/bin/pip3 install -r requirements.txt`
* Create .env: `cp env.template .venv` and fill in the missing pieces


## Using from IRSSI

If using from irssi autodl, you need to setup `~/.autodl/autodl.cfg`
The relevant config options are as below, however, don't forget the rest of the options.

    [options]
    upload-type = exec
    upload-command = <fullpath_to_project>/venv/bin/python3
    upload-args = <fullpath_to_project>/upload-torrent.py "$(TorrentPathName)"

`fullpath_to_project` could be `/home/Hammit/src/transmission-rpc-uploader` for example

