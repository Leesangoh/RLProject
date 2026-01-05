# RLProject

간단한 RL 학습 트랙(Atari DQN, Pykachu volleyball, Omok)을 실험용으로 모아둔 플레이스홀더 리포지토리입니다. 실제 구현은 비어 있으며, English keywords: reinforcement learning, DQN, Gymnasium, reproducibility, baseline scaffolding.

## Quickstart
- Setup: `python -m venv .venv && source .venv/bin/activate && pip install -e .`
- Atari placeholder run: `python projects/atari_dqn/train.py`
- Pykachu volleyball placeholder run: `python projects/pykachu_volleyball/train.py`
- Omok placeholder run: `python projects/omok/train.py`

## Reproducibility
- Plan to centralize seeding via config files (e.g., `projects/atari_dqn/config/dqn.yml`) and capture seeds in logs.
- Logging to be standardized with structured JSON + TensorBoard once implementation begins.
- Deterministic evaluation hooks and checkpoint naming conventions are TODO items across all tracks.

## Roadmap
- [ ] Atari DQN baseline with replay buffer + target network
- [ ] Pykachu volleyball Gymnasium env integration with scripted policies
- [ ] Omok agents (random / heuristic / self-play) and evaluation harness
- [ ] Common utilities for seeding, logging, and experiment tracking

## References
- https://velog.io/@frog_slayer/gym-Pykachu-volleyball
- https://ysl-iras.tistory.com/entry/Deep-RL-Course-DQN-%EC%8B%A4%EC%8A%B5-Atari-%EA%B2%8C%EC%9E%84
