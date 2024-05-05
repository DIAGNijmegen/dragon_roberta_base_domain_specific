#!/usr/bin/env bash
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

docker build -t joeranbosma/dragon_roberta_base_domain_specific:latest -t joeranbosma/dragon_roberta_base_domain_specific:v0.2.0 "$SCRIPTPATH"
