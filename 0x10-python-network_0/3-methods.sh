#!/bin/bash
# Print all HTTP methods that server of a URL will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
