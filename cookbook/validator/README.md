# Articles Validator

## Overview

The `articles_validator.ipynb` is a Jupyter Notebook designed to validate articles based on predefined criteria. This example helps create tool helps ensure that articles meet quality standards before publication.

## Features

- **Validation Checks**: The notebook performs various checks on the articles, including:
  - Title length
  - Content structure
  - Presence of required sections (e.g., introduction, conclusion)
  - Grammar and spelling checks

- **User-Friendly Interface**: The notebook provides an interactive interface for users to input articles and receive immediate feedback.

## Requirements

To run this notebook, you will need:

- Python 3.x
- Jupyter Notebook
- Required libraries (e.g., `pdfminer.six`, `langchain-gigachat`, `langchain-core`, `dotenv`, `getpass`)

You can install the necessary libraries using pip:

```bash
pip install pdfminer.six langchain-gigachat langchain-core dotenv getpass
```

## Usage

1. Open the `articles_validator.ipynb` in Jupyter Notebook.
2. Follow the instructions in the notebook to input your article.
3. Run the validation cells to check for compliance with the validation criteria.
