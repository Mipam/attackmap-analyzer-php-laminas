from .analyzer import PhpLaminasAnalyzer
from attackmap.sdk import AnalyzerMetadata

# SDK v2 (AC-403): re-exported module-level declaration, kept in sync with
# the class attribute on PhpLaminasAnalyzer.
EXTRACTION_PROTOCOL_VERSION = "2.0"

__all__ = [
    "AnalyzerMetadata",
    "EXTRACTION_PROTOCOL_VERSION",
    "PhpLaminasAnalyzer",
]
