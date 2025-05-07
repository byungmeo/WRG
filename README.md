# **'WRG(Weapon Recoil Generator)'**
## MCP Server Hosting Repository [![smithery badge](https://smithery.ai/badge/@Hyeongseob91/mcp-server)](https://smithery.ai/server/@Hyeongseob91/mcp-server)

## 주요 기능 / Key Features

- **Weapon Recoil Generation (WRG) 도구**  
  - `machinegun_recoil_points(shots: int)`  
    - 기관총 발사 횟수에 따른 반동 궤적 데이터를 생성합니다.  
    - Generates recoil trajectory data for a machine gun based on the number of shots.

- **Weapon Recoil Generation (WRG) Tool**  
  - `pistol_recoil_points(shots: int)`  
    - 권총 발사 횟수에 따른 반동 궤적 데이터를 생성합니다.  
    - Generates recoil trajectory data for a pistol based on the number of shots.

- **Weapon Recoil Generation (WRG) Tool**  
  - `shotgun_recoil_points(shots: int)`  
    - 산탄총 발사 횟수에 따른 반동 궤적 데이터를 생성합니다.  
    - Generates recoil trajectory data for a shotgun based on the number of shots.

- **MCP 엔드포인트 / MCP Endpoints**  
  - `/wrg/*`  
    - 웹 API 호출만으로 다양한 총기 반동 데이터를 손쉽게 획득할 수 있습니다.  
    - Provides easy access to various weapon recoil data via simple API calls.

- **Recoil Visualizer (RVZ) 도구 / Recoil Visualizer (RVZ) Tool**  
  - `plot_recoil_pattern(data: Tuple[List[float], List[float]])`  
    - 입력된 반동 좌표 데이터를 2D 산점도로 시각화합니다.  
    - Visualizes input recoil coordinate data as a 2D scatter plot.

- **MCP 엔드포인트 / MCP Endpoints**  
  - `/rvz/*`  
    - 브라우저 또는 클라이언트에서 즉시 시각화 결과를 확인할 수 있습니다.  
    - Enables instant visualization results through the browser or client.

- **원격·로컬 배포 지원 / Remote & Local Deployment**  
  - FastMCP 기반으로 로컬 서버뿐 아니라 클라우드 환경에도 동일한 API를 배포합니다.  
  - Deploys the same API to both local servers and cloud environments using FastMCP.

- **API Key 인증 기능 / API Key Authentication**  
  - 외부 사용자 접근 제어를 위한 API Key 인증 기능을 탑재할 예정입니다.  
  - Planned support for API Key authentication to control external access.

## 기대 효과 / Expected Benefits

1. **개발 생산성 극대화 / Productivity Boost**  
   - 복잡한 반동 모델링 코드를 직접 구현하지 않아도 됩니다.  
   - Eliminates the need to implement complex recoil modeling code yourself.  
   - 시각화 도구를 통해 데이터 검증 및 프로토타이핑 속도가 향상됩니다.  
   - Accelerates data validation and prototyping with built-in visualization tools.

2. **협업 및 재사용성 강화 / Enhanced Collaboration & Reusability**  
   - 통일된 MCP 인터페이스(`/wrg`, `/rvz`)로 팀원 간 기능 공유가 용이합니다.  
   - Facilitates feature sharing among team members through unified MCP interfaces (`/wrg`, `/rvz`).  
   - Backend/Frontend 및 AI 엔지니어와 게임 개발자 간 모듈 재사용이 가능합니다.  
   - Enables module reuse across backend/frontend, AI engineers, and game developers.

3. **유연한 배포·스케일링 / Flexible Deployment & Scaling**  
   - 로컬 테스트 후 클라우드에 바로 배포할 수 있어 트래픽 증가 시 손쉽게 확장 가능합니다.  
   - Allows immediate cloud deployment after local testing, making it easy to scale under increased traffic.  
   - CI/CD 파이프라인 연동으로 자동 배포 및 버전 관리를 지원합니다.  
   - Supports automated deployment and versioning via CI/CD pipeline integration.

4. **실시간 피드백 및 튜닝 지원 / Real-Time Feedback & Tuning**  
   - 게임 밸런스 조정 시 즉시 API 호출로 반동 패턴을 확인할 수 있습니다.  
   - Enables immediate recoil pattern checks via API calls during game balance adjustments.  
   - 데이터 기반 의사결정으로 플레이 테스트 효율성이 향상됩니다.  
   - Improves play-testing efficiency through data-driven decision making.


