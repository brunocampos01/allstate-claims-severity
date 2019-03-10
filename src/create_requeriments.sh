#!/usr/bin/env bash

pipreqs . --force

echo -e "\n\bRequirements this project:\n"
cat requirements.txt
