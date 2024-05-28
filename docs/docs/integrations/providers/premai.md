# PremAI

<<<<<<< HEAD
>[PremAI](https://app.premai.io) is a unified platform that lets you build powerful production-ready GenAI-powered applications with the least effort so that you can focus more on user experience and overall growth. 
=======
[PremAI](https://premai.io/) is an all-in-one platform that simplifies the creation of robust, production-ready applications powered by Generative AI. By streamlining the development process, PremAI allows you to concentrate on enhancing user experience and driving overall growth for your application. You can quickly start using our platform [here](https://docs.premai.io/quick-start).
>>>>>>> langchan/master


## ChatPremAI

This example goes over how to use LangChain to interact with different chat models with `ChatPremAI`

### Installation and setup

<<<<<<< HEAD
We start by installing langchain and premai-sdk. You can type the following command to install:
=======
We start by installing `langchain` and `premai-sdk`. You can type the following command to install:
>>>>>>> langchan/master

```bash
pip install premai langchain
```

<<<<<<< HEAD
Before proceeding further, please make sure that you have made an account on PremAI and already started a project. If not, then here's how you can start for free:

1. Sign in to [PremAI](https://app.premai.io/accounts/login/), if you are coming for the first time and create your API key [here](https://app.premai.io/api_keys/).

2. Go to [app.premai.io](https://app.premai.io) and this will take you to the project's dashboard. 

3. Create a project and this will generate a project-id (written as ID). This ID will help you to interact with your deployed application. 

4. Head over to LaunchPad (the one with 🚀 icon). And there deploy your model of choice. Your default model will be `gpt-4`. You can also set and fix different generation parameters (like max-tokens, temperature, etc) and also pre-set your system prompt. 

Congratulations on creating your first deployed application on PremAI 🎉 Now we can use langchain to interact with our application. 
=======
Before proceeding further, please make sure that you have made an account on PremAI and already created a project. If not, please refer to the [quick start](https://docs.premai.io/introduction) guide to get started with the PremAI platform. Create your first project and grab your API key.
>>>>>>> langchan/master

```python
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.chat_models import ChatPremAI
```

<<<<<<< HEAD
### Setup ChatPrem instance in LangChain 

Once we import our required modules, let's set up our client. For now, let's assume that our `project_id` is 8. But make sure you use your project-id, otherwise, it will throw an error.

To use langchain with prem, you do not need to pass any model name or set any parameters with our chat client. All of those will use the default model name and parameters of the LaunchPad model. 

`NOTE:` If you change the `model_name` or any other parameter like `temperature` while setting the client, it will override existing default configurations. 
=======
### Setup PremAI client in LangChain

Once we imported our required modules, let's setup our client. For now let's assume that our `project_id` is `8`. But make sure you use your project-id, otherwise it will throw error.

To use langchain with prem, you do not need to pass any model name or set any parameters with our chat-client. By default it will use the model name and parameters used in the [LaunchPad](https://docs.premai.io/get-started/launchpad). 

> Note: If you change the `model` or any other parameters like `temperature`  or `max_tokens` while setting the client, it will override existing default configurations, that was used in LaunchPad.   

>>>>>>> langchan/master

```python
import os
import getpass

if "PREMAI_API_KEY" not in os.environ:
    os.environ["PREMAI_API_KEY"] = getpass.getpass("PremAI API Key:")

chat = ChatPremAI(project_id=8)
```

<<<<<<< HEAD
### Calling the Model

Now you are all set. We can now start by interacting with our application. `ChatPremAI` supports two methods `invoke` (which is the same as `generate`) and `stream`. 

The first one will give us a static result. Whereas the second one will stream tokens one by one. Here's how you can generate chat-like completions. 

### Generation

=======
### Chat Completions

`ChatPremAI` supports two methods: `invoke` (which is the same as `generate`) and `stream`. 

The first one will give us a static result. Whereas the second one will stream tokens one by one. Here's how you can generate chat-like completions. 

>>>>>>> langchan/master
```python
human_message = HumanMessage(content="Who are you?")

chat.invoke([human_message])
```

<<<<<<< HEAD
The above looks interesting, right? I set my default launchpad system-prompt as: `Always sound like a pirate` You can also, override the default system prompt if you need to. Here's how you can do it. 
=======
You can provide system prompt here like this:
>>>>>>> langchan/master

```python
system_message = SystemMessage(content="You are a friendly assistant.")
human_message = HumanMessage(content="Who are you?")

chat.invoke([system_message, human_message])
```

You can also change generation parameters while calling the model. Here's how you can do that:

```python
chat.invoke(
    [system_message, human_message],
    temperature = 0.7, max_tokens = 20, top_p = 0.95
)
```

<<<<<<< HEAD

### Important notes:

Before proceeding further, please note that the current version of ChatPrem does not support parameters: [n](https://platform.openai.com/docs/api-reference/chat/create#chat-create-n) and [stop](https://platform.openai.com/docs/api-reference/chat/create#chat-create-stop) are not supported. 

We will provide support for those two above parameters in later versions. 

### Streaming

And finally, here's how you do token streaming for dynamic chat-like applications. 
=======
> If you are going to place system prompt here, then it will override your system prompt that was fixed while deploying the application from the platform. 

> Please note that the current version of ChatPremAI does not support parameters: [n](https://platform.openai.com/docs/api-reference/chat/create#chat-create-n) and [stop](https://platform.openai.com/docs/api-reference/chat/create#chat-create-stop). 

### Streaming

In this section, let's see how we can stream tokens using langchain and PremAI. Here's how you do it. 
>>>>>>> langchan/master

```python
import sys

for chunk in chat.stream("hello how are you"):
    sys.stdout.write(chunk.content)
    sys.stdout.flush()
```

<<<<<<< HEAD
Similar to above, if you want to override the system-prompt and the generation parameters, here's how you can do it. 
=======
Similar to above, if you want to override the system-prompt and the generation parameters, you need to add the following:
>>>>>>> langchan/master

```python
import sys

for chunk in chat.stream(
    "hello how are you",
    system_prompt = "You are an helpful assistant", temperature = 0.7, max_tokens = 20
):
    sys.stdout.write(chunk.content)
    sys.stdout.flush()
```

<<<<<<< HEAD
## Embedding

In this section, we are going to discuss how we can get access to different embedding models using `PremEmbeddings`. Let's start by doing some imports and defining our embedding object

```python
from langchain_community.embeddings import PremEmbeddings
```

Once we import our required modules, let's set up our client. For now, let's assume that our `project_id` is 8. But make sure you use your project-id, otherwise, it will throw an error.


```python

import os
import getpass
=======
This will stream tokens one after the other.

## PremEmbeddings

In this section we are going to dicuss how we can get access to different embedding model using `PremEmbeddings` with LangChain. Lets start by importing our modules and setting our API Key. 

```python
import os
import getpass
from langchain_community.embeddings import PremEmbeddings

>>>>>>> langchan/master

if os.environ.get("PREMAI_API_KEY") is None:
    os.environ["PREMAI_API_KEY"] = getpass.getpass("PremAI API Key:")

<<<<<<< HEAD
# Define a model as a required parameter here since there is no default embedding model

model = "text-embedding-3-large"
embedder = PremEmbeddings(project_id=8, model=model)
```

We have defined our embedding model. We support a lot of embedding models. Here is a table that shows the number of embedding models we support. 


| Provider    | Slug                                     | Context Tokens |
|-------------|------------------------------------------|----------------|
| cohere      | embed-english-v3.0                       | N/A            |
| openai      | text-embedding-3-small                   | 8191           |
| openai      | text-embedding-3-large                   | 8191           |
| openai      | text-embedding-ada-002                   | 8191           |
| replicate   | replicate/all-mpnet-base-v2              | N/A            |
| together    | togethercomputer/Llama-2-7B-32K-Instruct | N/A            |
| mistralai   | mistral-embed                            | 4096           |

To change the model, you simply need to copy the `slug` and access your embedding model. Now let's start using our embedding model with a single query followed by multiple queries (which is also called as a document)

```python
=======
```

We support lots of state of the art embedding models. You can view our list of supported LLMs and embedding models [here](https://docs.premai.io/get-started/supported-models). For now let's go for `text-embedding-3-large` model for this example. . 

```python

model = "text-embedding-3-large"
embedder = PremEmbeddings(project_id=8, model=model)

>>>>>>> langchan/master
query = "Hello, this is a test query"
query_result = embedder.embed_query(query)

# Let's print the first five elements of the query embedding vector

print(query_result[:5])
```
<<<<<<< HEAD

Finally, let's embed a document
=======
<Note>
Setting `model_name` argument in mandatory for PremAIEmbeddings unlike chat. 
</Note>

Finally, let's embed some sample document
>>>>>>> langchan/master

```python
documents = [
    "This is document1",
    "This is document2",
    "This is document3"
]

doc_result = embedder.embed_documents(documents)

# Similar to the previous result, let's print the first five element
# of the first document vector

print(doc_result[0][:5])
<<<<<<< HEAD
```
=======
```

```python
print(f"Dimension of embeddings: {len(query_result)}")
```
Dimension of embeddings: 3072

```python
doc_result[:5]
```
>Result:
>
>[-0.02129288576543331,
 0.0008162345038726926,
 -0.004556538071483374,
 0.02918623760342598,
 -0.02547479420900345]
>>>>>>> langchan/master
