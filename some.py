import openai

# Set your API key
openai.api_key = "sk-proj-lqYqAeJixmBAkX8t2F7xT3BlbkFJExuNCM03g2MoqIE6XlAt"

# Define the prompt for text completion
prompt = "Hello, how are you?"

# Make the API request
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the generated text
print(response.choices[0].text)