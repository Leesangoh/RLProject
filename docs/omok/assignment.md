# Overview
Omok 트랙은 격자 기반 보드게임 환경에서 정책 탐색 및 평가를 연습하는 과제입니다. 현재 환경과 에이전트는 모두 TODO로 비어 있습니다.

# Learning Objectives
- 턴제 보드게임 환경 정의와 상태 표현 설계
- 랜덤/휴리스틱/자기대전(self-play) 에이전트 비교
- 에피소드 롤아웃 로깅과 승률 통계 수집 계획 세우기

# Prerequisites
- Python 기초 및 RL 개념
- 게임 규칙(오목) 이해
- 테스트 주도 개발 경험(선택)

# Environment & API
- `projects/omok/envs/omok_env.py`에 Gymnasium 스타일 API를 설계 (reset/step/render TODO)
- 액션 스페이스: 보드 좌표 기반 Discrete 혹은 2D 인덱스 맵핑 예정
- 관찰: 보드 상태를 numpy 배열이나 flat vector로 표현

# Setup
- 가상환경: `python -m venv .venv && source .venv/bin/activate`
- 의존성 설치: `pip install -e .`
- 플레이스홀더 실행: `python projects/omok/train.py`

# Tasks
1. 환경 스펙을 정의하고 `omok_env.py`에 TODO 영역 채우기
2. `agents/random_agent.py`와 `agents/heuristic_agent.py`에 정책 스켈레톤 구현
3. `selfplay.py`에서 두 에이전트 대전 루프 설계
4. 로그/시드/재현성 계획 문서화 및 코드 주석 보강

# Evaluation
- 승률/무승부율을 최소 100 게임 기준으로 보고(실제 계산은 TODO)
- 실행 로그(현재는 "TODO: implement" 출력) 캡처 제출

# Deliverables
- 주석/설명 포함된 코드 파일
- 실험 설정과 관찰 포맷 설명 문서화

# Report Questions
- 보드 표현 방식이 탐색 효율과 관찰 공간 크기에 어떤 영향을 주는가?
- 휴리스틱 정책 설계 시 고려한 규칙 기반 전략은 무엇인가?
- 자기대전 과정에서 초기 정책이 결과에 미치는 영향은?

# Grading Rubric
- 40%: 환경/에이전트 설계 명확성
- 30%: 실험 계획 및 로그 구조
- 20%: 코드 주석과 TODO 처리 정도
- 10%: 확장 제안의 현실성

# Extensions
- MCTS 기반 에이전트 추가
- AlphaZero 스타일 self-play 파이프라인 설계
- 보드 크기/룰 변형 실험 및 밸런싱
