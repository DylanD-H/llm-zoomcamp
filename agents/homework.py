import random
from fastmcp import FastMCP


known_weather_data = {
    'berlin': 20.0
}

def get_weather(city: str) -> float:
    city = city.strip().lower()

    if city in known_weather_data:
        return known_weather_data[city]

    return round(random.uniform(-5, 35), 1)


get_weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Generates fake weather data",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "City to get the weather for"
            }
        },
        "required": ["city"],
        "additionalProperties": False
    }
}


def set_weather(city: str, temp: float) -> None:
    city = city.strip().lower()
    known_weather_data[city] = temp
    return 'OK'


set_weather_description = {
    "type": "function",
    "name": "set_weather",
    "description": "Set the weather for a city",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city to set the weather for",
            },
            "temp": {
                "type": "float",
                "description": "The temperature to set for the city",
            }
        },
        "required": ["city", "temp"],
        "additionalProperties": False
    }
}


mcp = FastMCP("Demo 🚀")

@mcp.tool
def get_weather(city: str) -> float:
    """
    Retrieves the temperature for a specified city.

    Parameters:
        city (str): The name of the city for which to retrieve weather data.

    Returns:
        float: The temperature associated with the city.
    """
    city = city.strip().lower()

    if city in known_weather_data:
        return known_weather_data[city]

    return round(random.uniform(-5, 35), 1)

@mcp.tool
def set_weather(city: str, temp: float) -> None:
    """
    Sets the temperature for a specified city.

    Parameters:
        city (str): The name of the city for which to set the weather data.
        temp (float): The temperature to associate with the city.

    Returns:
        str: A confirmation string 'OK' indicating successful update.
    """
    city = city.strip().lower()
    known_weather_data[city] = temp
    return 'OK'

if __name__ == "__main__":
    mcp.run()
