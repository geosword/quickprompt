# quickprompt
A simple python function to prompt Anthropic's Haiku and get a response back.
This was inspired by a suggestion by Michael and Chris Sharkey of the [This Day in AI Podcast](https://www.youtube.com/channel/UCwpNW6o_Kc13HQY5ol4rzsw) A weekly dive into the weeks AI news and well worth a listen!

## Use Case
The main idea is to reduce coding protentially complicated text processing functions, and instead, just get a (cheap) LLM
to do it.

## Why Haiku
Haiku scores better than GPT 3.5 on most benchmarks (Haiku's #7 to GPT3.5 #16 at time of writing) and is also multimodal, so really seems like a no brainer.

## Why NOT langchain
I've not used langchain, because the idea is to keep dependencies to a minimum, so you can copy-pasta this into your python project and start
using it straight away.

## Example
There is an example in the code, reproduced here:

```
email_content="Hello my name is John Doe, My number is 555-123-1234 and my email is john.doe@example.com, please send me information on your ABC Widget"
my_prompt = f"Extract information from this source data: {email_content}"
output_format = """
output in this json format:
{
    "name": "<extracted name here>",
    "telephone": "<extracted telephone here>",
    "email": "<extracted email address here>"
}
"""
my_prompt=f"{my_prompt}\n{output_format}"
extracted_information = quickprompt(my_prompt)
```

## Output
```
{
    "name": "John Doe",
    "telephone": "555-123-1234",
    "email": "john.doe@example.com"
}
```
