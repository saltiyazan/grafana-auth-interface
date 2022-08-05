#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.

"""Contains examples of provider and requirer charms for the grafana-auth interface."""

from ops.charm import CharmBase


class ExampleProviderCharm(CharmBase):
    """Example Provider Charm for grafana-auth config."""

    def __init__(self, *args):
        super().__init__(*args)
        """todo"""


class ExampleRequirerCharm(CharmBase):
    """Example Requirer Charm for grafana-auth config."""

    def __init__(self, *args):
        super().__init__(*args)
        """todo"""
