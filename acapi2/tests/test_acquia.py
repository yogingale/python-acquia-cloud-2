#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests_mock

from acapi2 import Acquia
from acapi2.exceptions import AcquiaCloudException
from acapi2.tests import BaseTest


@requests_mock.Mocker()
class TestAcquia(BaseTest):
    def test_failed_connection(self, mocker): pass

    def test_wrong_credentials_connection(self, mocker): pass

    def test_connection_system_health(self, mocker): pass
