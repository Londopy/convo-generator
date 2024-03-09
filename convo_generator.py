import csv
import time
import random
from datetime import datetime
from g4f.client import Client

sentences = []

for i in range(1001):
	time.sleep(1.5)

	client = Client()

	response = client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[{"role": "user", "content": "Simulate a basic conversation between two people. In csv style format."}]
	)

	time.sleep(1.5)

	sentences.append(response.choices[0].message.content)

	print(f"{i+1} generated")

	# handle interrupt
	if KeyboardInterrupt:
		break

current_time = datetime.now().strftime("%I.%M%p")  
random_num = random.randint(1,10000)

file_name = f'dataset{random_num}-{current_time}.csv'

with open(file_name, 'w') as f:
	writer = csv.writer(f)

	for i, sentence in enumerate(sentences):
		 writer.writerow([i, sentence])