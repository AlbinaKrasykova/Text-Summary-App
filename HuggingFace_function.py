#pip install transformers 
from transformers import pipeline

summarizer = pipeline("summarization")
ARTICLE = """

The error message "Token indices sequence length is longer than the specified maximum sequence length for this model" indicates that the input text you're providing to the model is longer than the maximum sequence length allowed by the model architecture. This issue arises because the model you're using has a maximum sequence length of 512 tokens, but the input text you're passing has more tokens than that.

This error typically occurs when you're trying to process long texts with models that have a limited maximum sequence length. To resolve this issue, you can try one of the following solutions:

Chunking or Truncating the Text: Break down your input text into smaller chunks or truncate it to fit within the maximum sequence length allowed by the model. This approach involves dividing your text into smaller segments and processing each segment separately.

Using a Different Model: Consider using a different model that supports longer input sequences. Some models are specifically designed to handle longer texts, such as BERT with Longformer or BigBird architectures.

Customizing the Model: Fine-tune the model to support longer input sequences by adjusting its architecture or parameters. However, this approach might require significant expertise in natural language processing and machine learning.

Utilizing Text Summarization Techniques: If your goal is text summarization, consider using techniques specifically designed for summarizing long texts, such as hierarchical summarization or extractive summarization.

"""
print(summarizer(ARTICLE, max_length=157, min_length=30, do_sample=False)) 
