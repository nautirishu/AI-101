from smolagents import CodeAgent, WebSearchTool, InferenceClientModel

@tool
def get_weather_date(city: str) -> dict:
    """
    Returns sample weather data of a city
    
    Args:
    city : name of the city
    """

    

model = InferenceClientModel()
agent = CodeAgent(tools=[WebSearchTool()], model=model, stream_outputs=True)

agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")