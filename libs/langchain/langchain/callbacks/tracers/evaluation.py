"""A tracer that runs evaluators over completed runs."""
<<<<<<< HEAD

=======
>>>>>>> langchan/master
from langchain_core.tracers.evaluation import (
    EvaluatorCallbackHandler,
    wait_for_all_evaluators,
)

__all__ = ["wait_for_all_evaluators", "EvaluatorCallbackHandler"]
