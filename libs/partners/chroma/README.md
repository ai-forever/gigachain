<<<<<<< HEAD
# gigachain-chroma
=======
# langchain-chroma
>>>>>>> langchan/master

This package contains the LangChain integration with Chroma.

## Installation

```bash
<<<<<<< HEAD
pip install -U gigachain-chroma
=======
pip install -U langchain-chroma
>>>>>>> langchan/master
```

## Usage

The `Chroma` class exposes the connection to the Chroma vector store.

```python
from langchain_chroma import Chroma

embeddings = ... # use a LangChain Embeddings class

vectorstore = Chroma(embeddings=embeddings)
```
