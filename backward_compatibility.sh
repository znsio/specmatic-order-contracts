#!/bin/bash

cat "The files that changed: $1"
echo "$1" | tr -s ' ' '\n' | xargs -I % java -jar ./tools/specmatic.jar compatible git commits % main HEAD