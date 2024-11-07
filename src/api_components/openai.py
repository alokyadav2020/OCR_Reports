from openai import OpenAI
import base64
import json
import os
from urllib.parse import urlparse



def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    



def openai_ocr(base64_img,api_key,models,prompt):
    client = OpenAI(api_key=api_key) #Best practice needs OPENAI_API_KEY environment variable
# client = OpenAI('OpenAI API Key here')

    response = client.chat.completions.create(
        model=models,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        # for online images
                        # "image_url": {"url": image_url}
                        "image_url": {"url": f"{base64_img}"}
                    }
                ],
            }
        ],
        max_tokens=4000,
    )

    txt_respone = response.choices[0].message.content
    total_token = response.usage.total_tokens

    return (txt_respone,total_token)




def merge_documents_with_openai(doc1, doc2, doc3,openai_key,prompt_user):
    

    client = OpenAI(api_key=openai_key)

    completion = client.chat.completions.create(
                                                    model="gpt-4o",
                                                    messages=[
                                                        {"role": "system", "content": "You are a helpful assistant."},
                                                        {
                                                            "role": "user",
                                                            "content": prompt_user
                                                        }
                                                    ]
                                                )
    result = completion.choices[0].message.content
    total_token = completion.usage.total_tokens
    return result,total_token
