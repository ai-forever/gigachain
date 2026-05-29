# Articles Validator

## Overview

The `articles_validator.py` is a file with functionality, designed to validate articles based on predefined criteria. This example helps create tool helps ensure that articles meet quality standards before publication.

## Features

- **Validation Checks**: The code performs various checks on the articles, including:
  - Title length
  - Content structure
  - Presence of required sections (e.g., introduction, conclusion)
  - Grammar and spelling checks

- **User-Friendly Interface**: The file provides an interactive interface for users to input articles and receive immediate feedback.

## Requirements

To run this code, you will need:

- Python 3.x
- Required libraries (e.g., `pdfminer.six`, `langchain-gigachat`, `langchain-core`, `dotenv`, `getpass`)

You can install the necessary libraries using pip:

```bash
pip install pdfminer.six langchain-gigachat dotenv getpass
```

## Usage

1. Open the `articles_validator.py`
2. Fill `GIGACHAT_CREDENTIALS` in '.env:
3. Input article_path for validation
4. Run the validation cells to check for compliance with the validation criteria.
