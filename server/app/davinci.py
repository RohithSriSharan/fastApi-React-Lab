import openai
from Test import products

# Set the API key
openai.api_key = "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"

# Test the authentication

prompt = "suggest a best air conditioner brand"
completions = openai.Completion.create(
    engine="text-curie-001",
    prompt=prompt,
    max_tokens=500,
)

query = completions["choices"][0]["text"]
print(query)

# Split the query string into individual words
query_words = query.split()

# Search for matching product names
for key, value in products.items():
    for product in value:
        for word in query_words:
            if word in product["name"]:
                print(product)
print(query_words)