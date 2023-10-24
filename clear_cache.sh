#!/bin/bash 
# finds all directories named .pytest_cache starting from the current directory (.) and removes them, using the + to execute the rm -rf command on multiple directories at once for efficiency.
find . -type d \( -name __pycache__ -o -name .pytest_cache \) -exec rm -rf {} +
