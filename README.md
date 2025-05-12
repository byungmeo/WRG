# <img src="/assets/target.png" alt="logo" width="32" style="vertical-align:middle;"/> Weapon Recoil Generator – build your own recoil MCP

* We released a versatile MCP server that lets FPS game developers generate and visualize weapon recoil patterns via simple API calls.
* FPS 게임 개발자가 간단한 API 호출만으로 무기 반동 패턴을 생성하고 시각화할 수 있는 강력한 MCP 서버를 출시했습니다.

## Learn more and deploy on Smithery: [![smithery badge](https://smithery.ai/badge/@Hyeongseob91/mcp-server)](https://smithery.ai/server/@Hyeongseob91/mcp-server)

# WRG MCP Server

* This MCP server provides two core tools—Weapon Recoil Generation and Recoil Visualization—exposed as HTTP endpoints. Simply deploy locally or in the cloud and start tuning your game’s recoil behavior in real time.
* 이 MCP 서버는 ‘무기 반동 생성’과 ‘반동 시각화’라는 두 가지 핵심 도구를 HTTP 엔드포인트로 제공하며, 로컬 또는 클라우드에 배포한 뒤 실시간으로 반동 튜닝을 시작할 수 있습니다.

## Installation

```bash
git clone https://github.com/Hyeongseob91/mcp-server.git
cd mcp-server
pip install -r requirements.txt
````

## Development

Run the server locally with automatic reload:
자동 리로드 기능을 켜고 로컬에서 서버를 실행합니다:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Usage

### Configure in Claude Desktop

Add to your Claude config:
Claude 설정 파일에 다음을 추가하세요:

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
Claude Desktop을 재시작한 후 /wrg와 /rvz 엔드포인트를 직접 호출할 수 있습니다.

## Key Features

* **Weapon Recoil Generation (WRG)**

  * `machinegun_recoil_points(shots: int)`

    * Generates recoil trajectory data for a machine gun based on the number of shots.
    * 기관총 발사 횟수에 따른 반동 궤적 데이터를 생성합니다.
  
* **Weapon Recoil Generation (WRG)**

  * `pistol_recoil_points(shots: int)`

    * Generates recoil trajectory data for a pistol based on the number of shots.
    * 권총 발사 횟수에 따른 반동 궤적 데이터를 생성합니다.

* **Weapon Recoil Generation (WRG)**

  * `shotgun_recoil_points(shots: int)`

    * Generates recoil trajectory data for a shotgun based on the number of shots.
    * 산탄총 발사 횟수에 따른 반동 궤적 데이터를 생성합니다.

* **Recoil Visualizer (RVZ)**

  * `plot_recoil_pattern(data: Tuple[List[float], List[float]])`

    * Visualizes input recoil coordinate data as a 2D scatter plot.
    * 입력된 반동 좌표 데이터를 2D 산점도로 시각화합니다.

* **MCP Endpoints**

  * `/wrg/*` – easy HTTP access to generate recoil data.
  * `/rvz/*` – instant HTTP access to visualize recoil patterns.

* **Remote & Local Deployment**

  * Deploy the same API to both local machines and cloud environments (e.g., Smithery) using FastMCP.
  * FastMCP를 사용하여 로컬 및 클라우드(예: Smithery) 환경에 동일한 API를 배포합니다.

* **API Key Authentication (Planned)**

  * Upcoming support for API keys to control external access.
  * 외부 접근 제어를 위한 API Key 인증 기능을 곧 지원할 예정입니다.

## Expected Benefits

1. **Productivity Boost**

   * No need to implement complex recoil algorithms yourself.
   * 복잡한 반동 알고리즘을 직접 구현할 필요가 없습니다.
   * Accelerates data validation and prototyping with built-in visualization tools.
   * 내장된 시각화 도구로 데이터 검증 및 프로토타입 속도가 향상됩니다.

2. **Enhanced Collaboration & Reusability**

   * Unified `/wrg` and `/rvz` interfaces make it easy for team members to share and reuse modules.
   * 통합된 /wrg 및 /rvz 인터페이스로 팀 간 모듈 공유 및 재사용이 용이합니다.
   * Works seamlessly across backend, frontend, AI engineers, and game developers.
   * 백엔드, 프론트엔드, AI 엔지니어, 게임 개발자 간 원활하게 연동됩니다.

3. **Flexible Deployment & Scaling**

   * Test locally, then deploy to the cloud for on-demand scaling.
   * 로컬 테스트 후 클라우드에 배포하여 필요에 따라 손쉽게 확장할 수 있습니다.
   * Integrates with CI/CD pipelines for automated deployment and version management.
   * CI/CD 파이프라인과 연동하여 자동 배포 및 버전 관리가 가능합니다.

4. **Real-Time Feedback & Tuning**

   * Instantly check recoil patterns via API calls during game balance adjustments.
   * 게임 밸런스 조정 시 API 호출로 즉시 반동 패턴을 확인할 수 있습니다.
   * Data-driven decision making improves play-test efficiency.
   * 데이터 기반 의사결정으로 플레이 테스트 효율성이 향상됩니다.

## Debugging

* Since this server communicates over HTTP, use verbose logging and the built-in reload flag. For deeper inspection, attach a debugger to the Uvicorn process or review the console error outputs.
* 이 서버는 HTTP로 통신하므로, 자세한 로깅과 --reload 플래그를 사용하세요. 보다 심층적인 검사를 위해 Uvicorn 프로세스에 디버거를 연결하거나 콘솔 오류 출력을 확인하면 됩니다.
