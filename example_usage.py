from client import VercelEdgeSpeedOptimizerClient
client = VercelEdgeSpeedOptimizerClient()
print(client.estimate_latency(1200))