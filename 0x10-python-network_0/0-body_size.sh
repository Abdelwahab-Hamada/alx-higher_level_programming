#!/bin/bash
# Get the byte size of the HTTP response for a URL.
curl -s "$1" | wc -c