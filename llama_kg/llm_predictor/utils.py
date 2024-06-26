from typing import Optional, Union
from llama_index.core.llms.llm import LLM
from langchain.base_language import BaseLanguageModel

from llama_kg.llm_predictor.KronLangChainLLM import KronLangChainLLM
from llama_index.llms.openai import OpenAI

from llama_index.core.llms.utils import LLMType


def kron_resolve_llm(llm: Optional[LLMType] = None) -> LLM:
    if isinstance(llm, BaseLanguageModel):
        # NOTE: if it's a langchain model, wrap it in a LangChainLLM
        return KronLangChainLLM(llm=llm)

    return llm or OpenAI()
