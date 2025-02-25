""" Various file io helpers
"""

from .tar import tar_doc_stream  # pylint: disable=W0406
from .text import (
    parse_mtl,  # pylint: disable=W0406
    parse_yaml,  # pylint: disable=W0406
    read_stdin_lines,  # pylint: disable=W0406
    slurp,  # pylint: disable=W0406
    slurp_lines,  # pylint: disable=W0406
)
from .timer import RateEstimator  # pylint: disable=W0406

from ._version import __version__  # pylint: disable=W0406

__all__ = (
    "parse_yaml",
    "read_stdin_lines",
    "slurp",
    "slurp_lines",
    "parse_mtl",
    "tar_doc_stream",
    "RateEstimator",
    "__version__",
)
