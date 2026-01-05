# Setup Guide

This repository only provides skeletons for RL study tracks. Every implementation is currently TODO.

## Environment
- Python 3.9+
- Recommended (Conda): `conda create -n rlproject python=3.11 -y && conda activate rlproject`
- Or use the env file: `conda env create -f environment.yml && conda activate rlproject`
- Install project editable: `pip install -e .`

## Structure
- Atari DQN: `projects/atari_dqn/`
- Pykachu volleyball: `projects/pykachu_volleyball/`
- Omok: `projects/omok/`

## References
- Pykachu: https://velog.io/@frog_slayer/gym-Pykachu-volleyball
- Atari DQN: https://ysl-iras.tistory.com/entry/Deep-RL-Course-DQN-%EC%8B%A4%EC%8A%B5-Atari-%EA%B2%8C%EC%9E%84

## Next Steps
- Run each project's `train.py` to confirm placeholder output before adding real logic.
