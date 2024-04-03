# Torrent Uploader for Transmission Daemon

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

`fullpath_to_project` could be `/home/byron/src/transmission-rpc-uploader` for example

