#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#
from abc import ABC, abstractmethod

from airbyte_cdk.sources.cac.types import Config


class Interpolation(ABC):
    @abstractmethod
    def eval(self, input_str: str, config: Config, **kwargs):  # FIXME: declare the output!
        # FIXME: also declare parameter types
        pass
