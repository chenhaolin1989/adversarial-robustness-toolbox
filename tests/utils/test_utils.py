# MIT License
#
# Copyright (C) The Adversarial Robustness Toolbox (ART) Authors 2020
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from __future__ import absolute_import, division, print_function, unicode_literals

import logging

import pytest

from art.utils import deprecated

logger = logging.getLogger(__name__)


class TestDeprecated:
    """
    Test the deprecation decorator functions and methods.
    """

    def test_deprecated_simple(self):
        @deprecated("1.3.0")
        def simple_addition(a, b):
            return a + b

        with pytest.deprecated_call():
            simple_addition(1, 2)

    def test_deprecated_reason_keyword(self, recwarn):
        @deprecated("1.3.0", reason="With some reason message.")
        def simple_addition(a, b):
            return a + b

        warn_msg_expected = (
            "Function 'simple_addition' is deprecated and will be removed in future release 1.3.0."
            "\nWith some reason message."
        )

        simple_addition(1, 2)
        warn_obj = recwarn.pop(DeprecationWarning)
        assert str(warn_obj.message) == warn_msg_expected

    def test_deprecated_replaced_by_keyword(self, recwarn):
        @deprecated("1.3.0", replaced_by="sum")
        def simple_addition(a, b):
            return a + b

        warn_msg_expected = (
            "Function 'simple_addition' is deprecated and will be removed in future release 1.3.0."
            " It will be replaced by 'sum'."
        )

        simple_addition(1, 2)
        warn_obj = recwarn.pop(DeprecationWarning)
        assert str(warn_obj.message) == warn_msg_expected
