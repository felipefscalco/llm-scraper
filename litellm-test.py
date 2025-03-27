from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()

os.environ['DEEPSEEK_API_KEY'] = os.getenv('DEEPSEEK_API_KEY')
response = completion(
    model="deepseek/deepseek-chat", 
    messages=[
       {"role": "user", "content": "hello from litellm"}
   ],
)
print(response)