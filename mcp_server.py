# mcp.py
from fastmcp import FastMCP
import sys
import io
import base64
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. MCP Server 설정 (HTTP 모드)
mcp = FastMCP(
    name="WSG",
    instructions="You are an AI assistant who utilizes tools that can help with game development",
    http=True
)

# 2. config
@mcp.tool()
def ping(config: dict = None):
    return {"status": "ok", "config": config}

# 3. Tool Definitions
## 3.1 Machinegun Recoil
@mcp.tool()
def machinegun_recoil_points(*, shots, config=None):
    """
    machinegun_recoil_points(shots: int):
    기관총 반동 궤적을 생성합니다. 
    반동이 강하고 연속적인 사격 패턴을 모사합니다.
    """
    try:
        shots = int(shots)
        if shots < 1 or shots > 100:
            raise ValueError
    except:
        raise ValueError("Shots must be an integer between 1 and 100")

    x, y = [], []
    for i in range(1, shots + 1):
        # 초탄
        if i <= int(shots/3):
            dx = np.random.uniform(0.0, 0.2)        # X축 흔들림 거의 없음
            dy = np.random.uniform(0.0, 0.65)       # Y축 미세 흔들림 증가
        # 중탄
        elif i <= int((shots/3)*2):
            dx = np.random.normal(0.1, 0.3)         # X축 미세 흔들림 증가
            dy = np.random.normal(0.1, 0.3)         # Y축 미세 흔들림 증가
        # 후탄
        else:
            dx = np.random.uniform(-1, 0.5)         # X축 흔들림 강함
            dy = np.random.normal(0.0 , 0.2)        # Y축 흔들림 거의 없음

        x.append(dx)
        y.append(dy)

    # x의 요소를 누적합으로 계산
    x_cum = np.cumsum(x)
    y_cum = np.cumsum(y)

    print(f'[DEBUG] machinegun_recoil_points called with shots={shots}', file=sys.stderr)
    return x_cum.tolist(), y_cum.tolist()

## 3.2 Pistol Recoil
@mcp.tool()
def pistol_recoil_points(*, shots, config=None):
    """
    pistol_recoil_points(shots: int):
    권총 반동 궤적을 생성합니다. 
    상대적으로 짧고 일관된 반동 패턴을 가집니다.
    """
    try:
        shots = int(shots)
        if shots < 1 or shots > 15:
            raise ValueError
    except:
        raise ValueError("shots must be an integer between 1 and 15")
    
    x, y = [], []
    for i in range(1, shots + 1):
        # 초탄
        if i <= int(shots/3):
            dx = np.random.uniform(0.0, 0.2)        # 약간의 X축 흔들림 부여
            dy = np.random.uniform(0.0, 0.5)        # 세로 반동 (조금 줄임)
        # 중탄
        elif i <= int((shots/3)*2):
            dx = np.random.uniform(0.3, 0.3)        # X축 미세 흔들림 증가
            dy = np.random.uniform(0.3, 0.3)
        # 후탄
        else:
            dx = np.random.uniform(-0.1, 0.3)       # X축 흔들림 강함
            dy = np.random.uniform(-0.1, 0.2)         # Y축 거의 없음

        x.append(dx)
        y.append(dy)

    # x의 요소를 누적합으로 계산
    x_cum = np.cumsum(x)
    y_cum = np.cumsum(y)

    print('...', file=sys.stderr)
    return x_cum.tolist(), y_cum.tolist()

## 3.3 Shotgun Recoil
@mcp.tool()
def shotgun_recoil_points(*, shots, pelletsPerShot, config=None):
    """
    shotgun_recoil_points(shots: int, pellets_per_shots: int):
    산탄총 반동 궤적을 생성합니다.
    퍼짐이 강한 산포형 탄착군을 모사합니다.
    """

    try:
        shots = int(shots)
        pelletsPerShot = int(pelletsPerShot)
        if shots < 1 or shots > 8:
            raise ValueError("shots must be an integer between 1 and 8")
        if pelletsPerShot < 4 or pelletsPerShot > 50:
         raise ValueError("pelletsPerShot must be an integer between 1 and 50")
    except:
        raise ValueError("shots and pelletsPerShot must be integers")
    
    x = []
    y = []
    for _ in range(shots):
        for _ in range(pelletsPerShot):
            dx = np.random.normal(0.0, 2.5)
            dy = np.random.normal(0.0, 2.5)
            x.append(dx)
            y.append(dy)

    print('...', file=sys.stderr)
    return x, y
    
## 3.4 Plot Recoil Pattern
@mcp.tool()
def plot_recoil_pattern(*, data, config=None):
    """생성된 좌표값을 시각화하는 메서드"""
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.scatter(data[0], data[1], s=10, marker='s')
    ax.axhline(0, linestyle='--', linewidth=1); ax.axvline(0, linestyle='--', linewidth=1)
    ax.set_facecolor('white'); ax.grid(True, linestyle=':', alpha=0.3)
    ax.set_xlim(-10, 10); ax.set_ylim(-10, 10); ax.set_aspect('equal')
    ax.set_title("Improved Recoil Pattern")
    plt.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format='png'); plt.close(fig)
    buf.seek(0)
    b64 = base64.b64encode(buf.read()).decode('ascii')

    print('...', file=sys.stderr)   
    return {"image/png;base64": b64}

## 3.5 Dataset Conversion
@mcp.tool()
def dataset(*, data, config=None):
    """생성된 좌표값을 데이터프레임화하는 메서드"""
    df = pd.DataFrame({"x": data[0], "y": data[1]})

    print('...', file=sys.stderr)     
    return df.to_dict(orient="records")

# 4. Server Start
if __name__ == "__main__":
    print("...", file=sys.stderr)
    mcp.run()