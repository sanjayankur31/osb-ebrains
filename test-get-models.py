#!/usr/bin/env python3
"""
Test getting a list of models from the EBRAINS API.
WIP

File: test-get-models.py

Copyright 2025 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""


from kg_core.kg import kg


DEV_URL = "core.kg-ppd.ebrains.eu"
kg_client = kg(DEV_URL).build()
