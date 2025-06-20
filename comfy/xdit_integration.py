import logging

try:
    import xdit
except ImportError:
    xdit = None
    logging.warning("xDit not installed, TACO-DiT will be unavailable")

class TACODiTWrapper:
    """Wrapper for xDit TACO-DiT acceleration.

    This class exposes a simplified interface to run models across multiple
    GPUs using xDit's TACO-DiT implementation. It is intentionally lightweight
    so that ComfyUI can make use of it without additional modifications.
    """

    def __init__(self, *args, **kwargs):
        if xdit is None:
            raise RuntimeError("xDit package is required for TACO-DiT support")
        self.engine = xdit.TACOEngine(*args, **kwargs)

    def execute(self, *args, **kwargs):
        return self.engine.run(*args, **kwargs)
