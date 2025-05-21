import langchain_ollama as lo

text = input()

brain = lo.OllamaLLM(model="tinyllama")

completion = brain.invoke(input=text)
print(completion)