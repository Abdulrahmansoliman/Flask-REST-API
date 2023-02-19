import requests

BASE = "http://127.0.0.1:5000/"


data = [{'likes': 10, 'name': 'Nothing good', 'views': 10000},
        {'likes': 10, 'name': 'bad days', 'views': 800},
        {'likes': 10, 'name': 'HELP!', 'views': 2000},
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.content)

input()
response = requests.get(BASE + "video/1")
print(response.json())
input()
response = requests.patch(BASE + "video/2", {"views": 99})
print(response.json())