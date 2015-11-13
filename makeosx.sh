#!/bin/bash
sudo rm -rf dist
sudo pyinstaller -i icons.icns -w mounter.pyw
sudo mv dist/mounter.app "Techknow WebDav.app"
sudo chmod 777 "Techknow WebDav.app"
sudo chown john:staff Techknow\ WebDav.app
