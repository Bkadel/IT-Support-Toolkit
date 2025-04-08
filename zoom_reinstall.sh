#!/bin/bash

echo "Uninstalling Zoom..."

# Uninstall Zoom (if it's installed via the default method)
sudo rm -rf /Applications/zoom.us.app

# Download and install Zoom
echo "Installing Zoom..."
curl -L https://zoom.us/client/latest/Zoom.pkg -o /tmp/Zoom.pkg
sudo installer -pkg /tmp/Zoom.pkg -target /

echo "Zoom installation complete."