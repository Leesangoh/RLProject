# Overview
Atari DQN 트랙은 클래식 Deep Q-Network 학습 파이프라인을 실습하는 과제입니다. 현재 코드는 비어 있으며, 학습 루프와 환경 로더를 직접 채워야 합니다.

# Learning Objectives
- DQN 구성 요소(리플레이 버퍼, 타깃 네트워크, 입실론-그리디 정책) 이해
- 실험 재현성을 위한 시드 관리와 로깅 설계 경험
- Gymnasium 기반 Atari 환경 인터페이스 숙련

# Prerequisites
- Python 및 PyTorch 기본 문법
- 강화학습 기초(Q-learning)
- YAML 설정 파일 읽기/편집 능력

# Environment & API
- Gymnasium Atari 환경 사용 예정 (`ALE/Pong-v5` 등)
- `render_mode`는 "rgb_array" 혹은 "human" 옵션 예정
- 액션 스페이스: Discrete, 환경별 액션 수 확인 필요
- 환경 초기화/step/reset 로직은 TODO (참고: https://ysl-iras.tistory.com/entry/Deep-RL-Course-DQN-%EC%8B%A4%EC%8A%B5-Atari-%EA%B2%8C%EC%9E%84)

# Setup
- 가상환경: `python -m venv .venv && source .venv/bin/activate`
- 의존성: `pip install -e .`
- 기본 실행(플레이스홀더): `python projects/atari_dqn/train.py`

# Tasks
1. `projects/atari_dqn/train.py`에 DQN 학습 루프 구현 (현재는 TODO 출력만 제공)
2. `projects/atari_dqn/eval.py`에 평가 루틴 추가
3. `projects/atari_dqn/config/dqn.yml`를 수정해 하이퍼파라미터 세팅
4. 시드와 로깅을 통합 관리하는 유틸을 설계하고 TODO 영역에 삽입

# Evaluation
- 제출자는 자체적으로 학습된 에이전트의 평균 에피소드 리워드 보고
- 실습에서는 최소 N=5 에피소드 평균 리워드와 분산을 기록(형식 자유)
- 현재 코드는 동작하지 않으므로 보고서 기준 평가는 TODO 채우기 정도로 진행

# Deliverables
- 수정한 코드 스냅샷(주석과 TODO 포함)
- 실행 로그 예시 (현재는 "TODO: implement" 출력 확인)
- 하이퍼파라미터 설정 파일 사본

# Report Questions
- 학습 중 불안정성을 줄이기 위한 선택지를 무엇을 적용했는지?
- 리플레이 버퍼 크기와 타깃 네트워크 업데이트 주기의 영향은?
- 참조 글(https://ysl-iras.tistory.com/entry/Deep-RL-Course-DQN-%EC%8B%A4%EC%8A%B5-Atari-%EA%B2%8C%EC%9E%84)에서 배운 포인트를 어떻게 반영했는지?

# Grading Rubric
- 40%: 코드 구조 완성도(TODO 대체 여부)
- 30%: 리포트에서의 실험 설계 설명
- 20%: 설정 파일 구성의 명확성
- 10%: 재현성 관련 시드/로깅 계획

# Extensions
- Double DQN, Dueling DQN, Prioritized Replay를 확장 과제로 제안
- NoisyNet, Rainbow 일부 모듈 추가 시도
- 프레임 스태킹 및 reward clipping 전략 비교 실험
