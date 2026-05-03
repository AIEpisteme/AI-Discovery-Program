import os
from openai import OpenAI

container_id="cntr_69aa0d29b5c88190bcea618cd4c75e0104c97b47bc11ce36"
file_id="cfile_69aa0e45ce9c819195c7e37a820bcffb"

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
file = client.containers.files.retrieve(
    file_id=file_id,
    container_id=container_id,
)
print(file.id)

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
content = client.containers.files.content.retrieve(
    file_id=file_id,
    container_id=container_id,
)
print(content)
data = content.read()
print(data)
