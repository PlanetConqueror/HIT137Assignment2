import torch
from transformers import AutoTokenizer

def count_unique_tokens(text_file_path, top_k=30):
  """Counts unique tokens in a text file and returns the top K most frequent words.

  Args:
    text_file_path: Path to the text file.
    top_k: Number of top frequent words to return.

  Returns:
    A list of tuples, where each tuple contains a word and its frequency.
  """

  with open(text_file_path, 'r', encoding='utf-8') as f:
    text = f.read()

  # Load the tokenizer, specifying the appropriate model name or path
  tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")  # Replace with your desired model

  # Tokenize the text
  input_ids = tokenizer.encode(text, return_tensors="pt")

  # Get the vocabulary and convert token IDs to words
  vocab = tokenizer.get_vocab()
  words = [vocab[token_id] for token_id in input_ids[0]]

  # Count token frequencies
  token_counts = torch.tensor([words.count(word) for word in vocab.values()])

  # Get top K most frequent words
  top_indices = torch.argsort(token_counts, descending=True)[:top_k]
  top_words = [(vocab[top_index], token_counts[top_index]) for top_index in top_indices]

  return top_words

# Example usage
text_file_path = "merged_data.txt"
top_words = count_unique_tokens(text_file_path)
print(top_words)