Ai_Agent = {'brand': 'OpenAI', 'model': 'GPT-4', 'year': 2023}
print(Ai_Agent['brand'])

# using get method
print(Ai_Agent.get('model'))

# Using keys() method
Ai_Agent['Usage'] = '87%'
Ai_Agent_keys = Ai_Agent.keys()
print(Ai_Agent_keys)

# Using values() method
Ai_Agent_values = Ai_Agent.values()
print(Ai_Agent_values)

# Using items() method
Ai_Agent_items = Ai_Agent.items()
print(Ai_Agent_items)