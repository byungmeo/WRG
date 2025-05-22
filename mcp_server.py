# mcp_server.py
from fastmcp import FastMCP
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. MCP Server 설정 (HTTP 모드)
mcp = FastMCP(
    name="WRG",
    instructions="You are an AI assistant who utilizes tools that can help with game development",
)

# 2. Tool Definitions
## 3.1 Machinegun Recoil
@mcp.tool()
def machinegun_recoil_points(shots):
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
            dx = np.random.uniform(0.0, 0.0)        # X축 흔들림 거의 없음
            dy = np.random.uniform(0.0, 0.3)       # Y축 미세 흔들림 증가
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

    return x_cum.tolist(), y_cum.tolist()

## 3.2 Pistol Recoil
@mcp.tool()
def pistol_recoil_points(shots):
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

    return x_cum.tolist(), y_cum.tolist()

## 3.3 Shotgun Recoil
@mcp.tool()
def shotgun_recoil_points(shots, pelletsPerShot=16):
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

    return x, y
    
## 3.4 Plot Recoil Pattern
@mcp.tool()
def plot_recoil_pattern(data):
    """생성된 좌표값을 시각화하는 메서드"""
    import ast
    
    # 문자열로 전달된 데이터를 파싱
    if isinstance(data, str):
        try:
            data = ast.literal_eval(data)
        except:
            return "Error: Invalid data format"
    
    # 데이터 검증
    if not isinstance(data, list) or len(data) != 2:
        return "Error: Data must be [x_list, y_list] format"
    
    x_coords, y_coords = data[0], data[1]
    
    plt.figure(figsize=(8, 8))
    plt.scatter(x_coords, y_coords, c='red', s=30, marker='s', alpha=0.7)
    
    # 궤적 연결선 추가
    plt.plot(x_coords, y_coords, 'b-', alpha=0.3, linewidth=1)
    
    # 시작점과 끝점 강조
    if len(x_coords) > 0:
        plt.scatter(x_coords[0], y_coords[0], c='green', s=100, marker='o', label='Start')
        plt.scatter(x_coords[-1], y_coords[-1], c='black', s=100, marker='x', label='End')
    
    plt.axhline(0, color='black', linestyle='--', linewidth=1)
    plt.axvline(0, color='black', linestyle='--', linewidth=1)
    
    plt.grid(True, linestyle=':', color='grey', alpha=0.3)
    plt.gca().invert_yaxis()  # y축 반전
    
    plt.title(f"Recoil Pattern ({len(x_coords)} shots)")
    plt.xlabel("Horizontal Deviation")
    plt.ylabel("Vertical Recoil")
    plt.legend()
    
    # 이미지를 Base64로 인코딩하여 반환
    import io
    import base64
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=150, bbox_inches='tight')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode()
    plt.close()  # 메모리 정리
    
    return f"data:image/png;base64,{image_base64}"

## 3.5 Dataset Conversion
@mcp.tool()
def dataset(data):
    """생성된 좌표값을 데이터프레임화하는 메서드"""
    import ast
    
    # 문자열로 전달된 데이터를 파싱
    if isinstance(data, str):
        try:
            data = ast.literal_eval(data)
        except:
            return [{"error": "Invalid data format"}]
    
    # 데이터 검증
    if not isinstance(data, list) or len(data) != 2:
        return [{"error": "Data must be [x_list, y_list] format"}]
    
    x_coords, y_coords = data[0], data[1]
    
    # 길이 검증
    if len(x_coords) != len(y_coords):
        return [{"error": "X and Y coordinates length mismatch"}]
    
    # 데이터프레임 생성 및 추가 정보 포함
    records = []
    for i, (x, y) in enumerate(zip(x_coords, y_coords)):
        records.append({
            "shot_number": i + 1,
            "x_coordinate": round(x, 4),
            "y_coordinate": round(y, 4),
            "distance_from_center": round((x**2 + y**2)**0.5, 4),
            "cumulative_recoil": round(sum(y_coords[:i+1]), 4)
        })
    
    return records

# 4. Server Start
if __name__ == "__main__":
    mcp.run(transport='stdio')