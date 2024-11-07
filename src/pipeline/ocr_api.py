from src.api_components.anthropic import ocr_anthropic
from src.api_components.documentsai import ocr_doc
from src.api_components.openai import openai_ocr
from src.Utils.common import encode_image
from src.entity_variables.llm_api_entity import AnthropicKeyVariables,OpenaiKeyVariables,DocumentaiKeyVariables
from dotenv import load_dotenv
from google.oauth2 import service_account








class OCR_API_LIST:
    def __init__(self) -> None:
        
        self._AnthropicKeyVariables = AnthropicKeyVariables()
        self._OpenaiKeyVariables = OpenaiKeyVariables()
        self._DocumentaiKeyVariables = DocumentaiKeyVariables()


    def anthropic_api(self,image_base64):
        
        response_anthropic,token_enthropic = ocr_anthropic(image_strin=image_base64,
                                           api_key=self._AnthropicKeyVariables.anthropict_api_key,
                                           prompt=self._AnthropicKeyVariables.prompt,
                                           MODEL_NAME=self._AnthropicKeyVariables.anthropic_model)

        return response_anthropic,token_enthropic




    def document_ai_api(self,image):


        response_documentai,accuracy_documentai = ocr_doc(PROCESSOR_ID=self._DocumentaiKeyVariables.PROJECT_ID,
                                                          PROJECT_ID=self._DocumentaiKeyVariables.PROJECT_ID,
                                                          LOCATION=self._DocumentaiKeyVariables.LOCATION,
                                                          FILE_PATH=image,
                                                          credentials=self._DocumentaiKeyVariables.credentials
                                                          )
        

        return response_documentai,accuracy_documentai



    def open_ai_api(self,image_base64):
        response_openai,token_openai = openai_ocr(base64_img=image_base64,
                                                  api_key=self._OpenaiKeyVariables.openai_api_key,
                                                  models=self._OpenaiKeyVariables.openai_model,
                                                  prompt=self._OpenaiKeyVariables.prompt)
        


        return response_openai,token_openai
        


