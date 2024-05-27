#!/bin/env bash

git config --local --get include.path | grep -e ../.gitconfig || git config --local --add include.path ../.gitconfig

[ -f "$(git rev-parse --show-toplevel)/requirements.txt" ] && pip3 install --user -r "$(git rev-parse --show-toplevel)/requirements.txt" || echo no "requirements.txt" file