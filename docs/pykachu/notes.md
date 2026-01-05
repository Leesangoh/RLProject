# Pykachu Volleyball Notes

- 참고: https://velog.io/@frog_slayer/gym-Pykachu-volleyball
- 환경은 Gymnasium 호환 형태로 설계 예정이며 `render_mode`는 "rgb_array" 또는 "human" 옵션을 사용할 계획입니다.
- 액션 스페이스는 Discrete 형태로 점프/이동/스파이크 등을 매핑할 예정입니다.
- `env/pykachu_env.py`는 reset/step/render/close 시그니처만 주석 형태로 남겨 두었으며 실제 구현은 TODO입니다.
- 정책/학습 루프 역시 비어 있으며, 학습/평가/랜덤 플레이 스크립트가 모두 placeholder 출력만 제공합니다.
