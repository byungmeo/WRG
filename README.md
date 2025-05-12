# WRG (Weapon Recoil Generator) – build your own recoil MCPs

We released a versatile MCP server that lets FPS game developers generate and visualize weapon recoil patterns via simple API calls.

Learn more and deploy on Smithery: [![smithery badge](https://smithery.ai/badge/@Hyeongseob91/mcp-server)](https://smithery.ai/server/@Hyeongseob91/mcp-server)

# WRG MCP Server

This MCP server provides two core tools—Weapon Recoil Generation and Recoil Visualization—exposed as HTTP endpoints. Simply deploy locally or in the cloud and start tuning your game’s recoil behavior in real time.

## Installation

```bash
git clone https://github.com/Hyeongseob91/mcp-server.git
cd mcp-server
pip install -r requirements.txt
````

## Development

Run the server locally with automatic reload:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Usage

### Configure in Claude Desktop

Add to your Claude config:

* **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
* **Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "wrg": {
      "command": "python /path/to/mcp-server/main.py --http"
    }
  }
}
```

After restarting Claude Desktop, you can call the `/wrg` and `/rvz` endpoints directly.

## Key Features

* **Weapon Recoil Generation (WRG)**

  * `machinegun_recoil_points(shots: int)`

    * Generates recoil trajectory data for a machine gun based on the number of shots.

* **Weapon Recoil Generation (WRG)**

  * `pistol_recoil_points(shots: int)`

    * Generates recoil trajectory data for a pistol based on the number of shots.

* **Weapon Recoil Generation (WRG)**

  * `shotgun_recoil_points(shots: int)`

    * Generates recoil trajectory data for a shotgun based on the number of shots.

* **Recoil Visualizer (RVZ)**

  * `plot_recoil_pattern(data: Tuple[List[float], List[float]])`

    * Visualizes input recoil coordinate data as a 2D scatter plot.

* **MCP Endpoints**

  * `/wrg/*` – easy HTTP access to generate recoil data.
  * `/rvz/*` – instant HTTP access to visualize recoil patterns.

* **Remote & Local Deployment**

  * Deploy the same API to both local machines and cloud environments (e.g., Smithery) using FastMCP.

* **API Key Authentication (Planned)**

  * Upcoming support for API keys to control external access.

## Expected Benefits

1. **Productivity Boost**

   * No need to implement complex recoil algorithms yourself.
   * Accelerates data validation and prototyping with built-in visualization tools.

2. **Enhanced Collaboration & Reusability**

   * Unified `/wrg` and `/rvz` interfaces make it easy for team members to share and reuse modules.
   * Works seamlessly across backend, frontend, AI engineers, and game developers.

3. **Flexible Deployment & Scaling**

   * Test locally, then deploy to the cloud for on-demand scaling.
   * Integrates with CI/CD pipelines for automated deployment and version management.

4. **Real-Time Feedback & Tuning**

   * Instantly check recoil patterns via API calls during game balance adjustments.
   * Data-driven decision making improves play-test efficiency.

## Debugging

Since this server communicates over HTTP, use verbose logging and the built-in reload flag. For deeper inspection, attach a debugger to the Uvicorn process or review the console error outputs.
