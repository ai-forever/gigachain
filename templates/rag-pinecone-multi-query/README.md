# RAG - Pinecone - multi-query

This template performs RAG using `Pinecone` and `OpenAI` with a multi-query retriever. 

It uses an LLM to generate multiple queries from different perspectives based on the user's input query. 

For each query, it retrieves a set of relevant documents and takes the unique union across all queries for answer synthesis.

## Environment Setup

This template uses Pinecone as a vectorstore and requires that `PINECONE_API_KEY`, `PINECONE_ENVIRONMENT`, and `PINECONE_INDEX` are set. 

Set the `OPENAI_API_KEY` environment variable to access the OpenAI models.

## Usage

To use this package, you should first install the LangChain CLI:

```shell
pip install -U gigachain-cli
```

To create a new LangChain project and install this package, do:

```shell
gigachain app new my-app --package rag-pinecone-multi-query
```

To add this package to an existing project, run:

```shell
gigachain app add rag-pinecone-multi-query
```

And add the following code to your `server.py` file:

```python
from rag_pinecone_multi_query import chain as rag_pinecone_multi_query_chain

add_routes(app, rag_pinecone_multi_query_chain, path="/rag-pinecone-multi-query")
```

(Optional) Now, let's configure LangSmith. LangSmith will help us trace, monitor, and debug LangChain applications. You can sign up for LangSmith [here](https://smith.langchain.com/). If you don't have access, you can skip this section

```shell
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=<your-api-key>
export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"
```

If you are inside this directory, then you can spin up a LangServe instance directly by:

```shell
gigachain serve
```

This will start the FastAPI app with a server running locally at [http://localhost:8000](http://localhost:8000)

You can see all templates at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
You can access the playground at [http://127.0.0.1:8000/rag-pinecone-multi-query/playground](http://127.0.0.1:8000/rag-pinecone-multi-query/playground)

To access the template from code, use:

```python
from langserve.client import RemoteRunnable

runnable = RemoteRunnable("http://localhost:8000/rag-pinecone-multi-query")
```