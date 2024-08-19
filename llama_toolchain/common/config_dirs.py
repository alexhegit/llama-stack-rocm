# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import os
from pathlib import Path


LLAMA_STACK_CONFIG_DIR = Path(os.path.expanduser("~/.llama/"))

DISTRIBS_BASE_DIR = LLAMA_STACK_CONFIG_DIR / "distributions"

DEFAULT_CHECKPOINT_DIR = LLAMA_STACK_CONFIG_DIR / "checkpoints"