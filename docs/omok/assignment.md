# Overview
The Omok track is an assignment for grid-based board-game environments focusing on policy exploration and evaluation. All environment and agent code is currently TODO.

# Learning Objectives
- Define turn-based board-game environments and state representations
- Compare random, heuristic, and self-play agents
- Plan episode rollout logging and win-rate statistics

# Prerequisites
- Python basics and RL concepts
- Knowledge of Omok rules
- Optional: experience with test-driven development

# Environment & API
- Design a Gymnasium-style API in `projects/omok/envs/omok_env.py` (reset/step/render TODO)
- Action space: map board coordinates to Discrete or 2D index
- Observation: board state as numpy array or flattened vector

# Setup
- Conda env: `conda create -n rlproject python=3.11 -y && conda activate rlproject`
- Or: `conda env create -f environment.yml && conda activate rlproject`
- Install dependencies: `pip install -e .`
- Placeholder run: `python projects/omok/train.py`

# Tasks
1. Specify the environment and fill TODOs in `omok_env.py`
2. Add policy skeletons in `agents/random_agent.py` and `agents/heuristic_agent.py`
3. Design the match loop in `selfplay.py` for two-agent play
4. Document logging/seed/reproducibility plans and comment the code

# Evaluation
- Report win/draw rates over at least 100 games (calculation is TODO for now)
- Provide sample logs (currently just "TODO: implement" output)

# Deliverables
- Commented code files with TODO guidance
- Documentation of experiment settings and observation formats

# Report Questions
- How does board representation impact exploration efficiency and observation size?
- What rule-based strategies were considered for the heuristic policy?
- How does the initial policy affect outcomes during self-play?

# Grading Rubric
- 40%: Clarity of environment/agent design
- 30%: Experiment plan and logging structure
- 20%: Code comments and TODO completion
- 10%: Realism of extension proposals

# Extensions
- Add an MCTS-based agent
- Design an AlphaZero-style self-play pipeline
- Experiment with different board sizes/rules and balance adjustments
