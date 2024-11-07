from src.api_components.openai import merge_documents_with_openai
from src.entity_variables.llm_api_entity import OpenaiKeyVariables
from src.entity_variables.promt import prompt_for_merge_document





class LLM_API_LIST:
    def __init__(self) -> None:
        self._OpenaiKeyVariables = OpenaiKeyVariables()
        self._prompt_for_merge_document = prompt_for_merge_document



    def merge_with_openai(self,doc1, doc2, doc3):

        txt_merge, tokensopenai = merge_documents_with_openai(doc1=doc1,
                                    doc2=doc2,
                                    doc3=doc3,
                                    openai_key=self._OpenaiKeyVariables.openai_api_key,
                                    prompt_user=self._prompt_for_merge_document
                                    )

        return txt_merge, tokensopenai                            
