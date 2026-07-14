class AgentRegistry:

    def __init__(self):

        self._agents = {}

    def register(self, agent):

        self._agents[agent.name] = agent

    def get(self, name):

        if name not in self._agents:

            raise ValueError(
                f"Agent '{name}' is not registered."
            )

        return self._agents[name]

    def list(self):

        return list(self._agents.keys())
    
    
