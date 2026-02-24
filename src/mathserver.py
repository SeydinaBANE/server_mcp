from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MATH")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Additionne deux nombres et retourne le résultat"""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Soustrait b de a et retourne le résultat"""
    return a - b

if __name__ == "__main__":
    mcp.run(transport="stdio")