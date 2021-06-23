#!/bin/bash

expressvpn status  >> result.txt

rkhunter --check --sk >> result.txt
