import docker 

# client = docker.DockerClient(base_url='unix://var/run/docker.sock')
client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')

for event in client.events(decode=True):
        print(event)
