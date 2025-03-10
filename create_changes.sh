#!/bin/bash

# Create the changes directory
mkdir -p changes

# Copy the file 100 times with the prefix <index>_
for i in {1..100}; do
  cp io/specmatic/examples/store/openapi/api_order_v3.yaml changes/${i}_api_order_v3.yaml
done
