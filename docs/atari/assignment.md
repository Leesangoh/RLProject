# Overview
The Atari DQN track is a hands-on assignment for building a classic Deep Q-Network pipeline. Code is currently empty; you must fill in the training loop and environment loader.

# Learning Objectives
- Understand DQN components: replay buffer, target network, epsilon-greedy policy
- Practice seed management and logging design for reproducibility
- Gain fluency with Gymnasium Atari environment interfaces

# Prerequisites
- Python and PyTorch basics
- Reinforcement learning fundamentals (Q-learning)
- Ability to read and edit YAML config files

# Environment & API
- Uses Gymnasium Atari environments (e.g., `ALE/Pong-v5`)
- `render_mode` planned options: "rgb_array" or "human"
- Action space: Discrete; verify action count per environment
- Env init/reset/step logic is TODO (reference: https://ysl-iras.tistory.com/entry/Deep-RL-Course-DQN-%EC%8B%A4%EC%8A%B5-Atari-%EA%B2%8C%EC%9E%84)

# Setup
- Virtualenv: `python -m venv .venv && source .venv/bin/activate`
- Dependencies: `pip install -e .`
- Placeholder run: `python projects/atari_dqn/train.py`

# Tasks
1. Implement the DQN training loop in `projects/atari_dqn/train.py` (currently prints TODO)
2. Add evaluation routine in `projects/atari_dqn/eval.py`
3. Tune hyperparameters in `projects/atari_dqn/config/dqn.yml`
4. Design utilities for seeds and logging, then integrate into TODO regions

# Evaluation
- Report average episode reward over at least N=5 episodes for trained agents
- For now, grading is based on TODO replacement and documentation, since code does not run

# Deliverables
- Updated code snapshots (with comments and TODO replacements)
- Example logs (currently the "TODO: implement" output)
- Copy of the hyperparameter config

# Report Questions
- What stability tricks did you apply to reduce training variance?
- How did replay buffer size and target network update frequency affect learning?
- How did you incorporate insights from https://ysl-iras.tistory.com/entry/Deep-RL-Course-DQN-%EC%8B%A4%EC%8A%B5-Atari-%EA%B2%8C%EC%9E%84?

# Grading Rubric
- 40%: Code structure completeness (TODO replacements)
- 30%: Experimental design clarity in the report
- 20%: Quality of configuration files
- 10%: Reproducibility plan (seeds/logging)

# Extensions
- Try Double DQN, Dueling DQN, or Prioritized Replay
- Experiment with NoisyNet or Rainbow components
- Compare frame stacking and reward clipping strategies
