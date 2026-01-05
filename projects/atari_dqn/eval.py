import gymnasium as gym
from pyvirtualdisplay import Display
import ale_py

# 1. 디스플레이를 먼저 띄웁니다 (visible=1 설정)
# 주의: 이 코드가 실행되려면 아까 말씀드린 Xephyr가 설치되어 있어야 합니다.
virtual_display = Display(visible=1, size=(600, 400))
virtual_display.start()

# 2. Gym 환경 생성
# 핵심: render_mode="human"으로 해야 팝업 창이 뜹니다.
env = gym.make("BreakoutNoFrameskip-v4", render_mode="human")

state, info = env.reset()

# 3. 게임 루프 실행
# 루프가 도는 동안 가상 디스플레이 창에 게임 화면이 계속 갱신됩니다.
try:
    while True:
        action = env.action_space.sample()  # 여기서는 랜덤 행동 (나중엔 모델이 결정)
        print("action: ", action)
        state, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            state, info = env.reset()
            
except KeyboardInterrupt:
    print("Game Over")
finally:
    env.close()
    virtual_display.stop()