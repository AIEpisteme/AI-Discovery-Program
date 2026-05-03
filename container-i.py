import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
page = client.containers.list()
page = page.data[0]
print(page.id)

#container id: cntr_69aa0d29b5c88190bcea618cd4c75e0104c97b47bc11ce36
#file id: cfile_69a785d5f0f8819197f081b44b0880a3
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
page = client.containers.files.list(
    container_id="cntr_69aa0d29b5c88190bcea618cd4c75e0104c97b47bc11ce36",
)
page = page.data[0]
print(page.id)
