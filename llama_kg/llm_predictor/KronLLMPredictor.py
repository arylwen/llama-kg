
from typing import Any, Generator, Optional, Protocol, Tuple, runtime_checkable

from llama_index.core.service_context_elements.llm_predictor import  LLMPredictor
from llama_index.core.llms.utils import LLMType
from llama_index.core.callbacks.base import CallbackManager

from llama_kg.llm_predictor.utils import kron_resolve_llm

class KronLLMPredictor(LLMPredictor):
    """LLM predictor class.

    Wrapper around an LLMChain from Langchain.

    Args:
        llm (Optional[langchain.llms.base.LLM]): LLM from Langchain to use
            for predictions. Defaults to OpenAI's text-davinci-003 model.
            Please see `Langchain's LLM Page
            <https://langchain.readthedocs.io/en/latest/modules/llms.html>`_
            for more details.

        retry_on_throttling (bool): Whether to retry on rate limit errors.
            Defaults to true.

        cache (Optional[langchain.cache.BaseCache]) : use cached result for LLM
    """

    def __init__(
        self,
        llm: Optional[LLMType] = None,
        callback_manager: Optional[CallbackManager] = None,
     ) -> None:
        """Initialize params."""
        super().__init__(llm=llm, callback_manager=callback_manager)
        self._llm = kron_resolve_llm(llm)
        #self.callback_manager = callback_manager or CallbackManager([])




