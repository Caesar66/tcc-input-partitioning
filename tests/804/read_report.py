import json

with open('log.json', 'r') as f:
	parsed = [json.loads(line) for line in f.readlines()]
	print(json.dumps(parsed, indent=4))
