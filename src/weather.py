from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """get weather"""
    return "il pleut pas au senegal"

if __name__=="__main__":
    mcp.run(transport="streamable-http")