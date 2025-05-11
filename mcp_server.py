import asyncio
import sys
import base64
import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from mcp.server import Server
from mcp.server.models import InitializationOptions, NotificationOptions
import mcp.types as types
import mcp.server.stdio

server = Server("weapon_recoil_server")

### TOOL 1: machinegun_recoil_points
@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="machinegun_recoil_points",
            description="Generate recoil pattern for machinegun",
            inputSchema={
                "type": "object",
                "properties": {
                    "shots": {"type": "integer", "description": "Number of shots"},
                },
                "required": ["shots"]
            },
        ),
        types.Tool(
            name="pistol_recoil_points",
            description="Generate recoil pattern for pistol",
            inputSchema={
                "type": "object",
                "properties": {
                    "shots": {"type": "integer", "description": "Number of shots"},
                },
                "required": ["shots"]
            },
        ),
        types.Tool(
            name="shotgun_recoil_points",
            description="Generate recoil pattern for shotgun",
            inputSchema={
                "type": "object",
                "properties": {
                    "shots": {"type": "integer"},
                    "pelletsPerShot": {"type": "integer"},
                },
                "required": ["shots", "pelletsPerShot"]
            },
        ),
        types.Tool(
            name="plot_recoil_pattern",
            description="Plot recoil pattern from data",
            inputSchema={
                "type": "object",
                "properties": {
                    "data": {"type": "array", "items": {"type": "array", "items": {"type": "number"}}}
                },
                "required": ["data"]
            },
        ),
        types.Tool(
            name="dataset",
            description="Convert recoil data to DataFrame",
            inputSchema={
                "type": "object",
                "properties": {
                    "data": {"type": "array", "items": {"type": "array", "items": {"type": "number"}}}
                },
                "required": ["data"]
            },
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict | None) -> list[types.TextContent]:
    try:
        if name == "machinegun_recoil_points":
            shots = int(arguments.get("shots", 10))
            x, y = [], []
            for i in range(1, shots + 1):
                if i <= shots / 3:
                    dx = np.random.uniform(0.0, 0.2)
                    dy = np.random.uniform(0.0, 0.65)
                elif i <= (shots / 3) * 2:
                    dx = np.random.normal(0.1, 0.3)
                    dy = np.random.normal(0.1, 0.3)
                else:
                    dx = np.random.uniform(-1, 0.5)
                    dy = np.random.normal(0.0, 0.2)
                x.append(dx)
                y.append(dy)
            x_cum = np.cumsum(x).tolist()
            y_cum = np.cumsum(y).tolist()
            return [types.TextContent(type="text", text=f"{x_cum}\n{y_cum}")]

        elif name == "pistol_recoil_points":
            shots = int(arguments.get("shots", 10))
            x, y = [], []
            for i in range(1, shots + 1):
                if i <= shots / 3:
                    dx = np.random.uniform(0.0, 0.2)
                    dy = np.random.uniform(0.0, 0.5)
                elif i <= (shots / 3) * 2:
                    dx = 0.3
                    dy = 0.3
                else:
                    dx = np.random.uniform(-0.1, 0.3)
                    dy = np.random.uniform(-0.1, 0.2)
                x.append(dx)
                y.append(dy)
            x_cum = np.cumsum(x).tolist()
            y_cum = np.cumsum(y).tolist()
            return [types.TextContent(type="text", text=f"{x_cum}\n{y_cum}")]

        elif name == "shotgun_recoil_points":
            shots = int(arguments.get("shots", 5))
            pellets = int(arguments.get("pelletsPerShot", 10))
            x, y = [], []
            for _ in range(shots):
                for _ in range(pellets):
                    dx = np.random.normal(0.0, 2.5)
                    dy = np.random.normal(0.0, 2.5)
                    x.append(dx)
                    y.append(dy)
            return [types.TextContent(type="text", text=f"{x}\n{y}")]

        elif name == "plot_recoil_pattern":
            data = arguments.get("data")
            fig, ax = plt.subplots(figsize=(5, 5))
            ax.scatter(data[0], data[1], s=10, marker='s')
            ax.axhline(0, linestyle='--', linewidth=1)
            ax.axvline(0, linestyle='--', linewidth=1)
            ax.set_facecolor('white')
            ax.grid(True, linestyle=':', alpha=0.3)
            ax.set_xlim(-10, 10)
            ax.set_ylim(-10, 10)
            ax.set_aspect('equal')
            plt.tight_layout()
            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            plt.close(fig)
            buf.seek(0)
            b64 = base64.b64encode(buf.read()).decode('ascii')
            return [types.TextContent(type="image", image={"format": "png", "data": b64})]

        elif name == "dataset":
            data = arguments.get("data")
            df = pd.DataFrame({"x": data[0], "y": data[1]})
            return [types.TextContent(type="text", text=df.to_string(index=False))]

        else:
            raise ValueError("Unknown tool")

    except Exception as e:
        return [types.TextContent(type="text", text=f"[ERROR] {str(e)}")]

async def main():
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="weapon_recoil_server",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            )
        )

if __name__ == "__main__":
    asyncio.run(main())
