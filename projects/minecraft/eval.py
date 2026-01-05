import minedojo
from pyvirtualdisplay import Display
import numpy as np
import time

virtual_display = Display(visible=1, size=(2048, 1536)) 
virtual_display.start()

env = minedojo.make(
    task_id="open-ended",
    image_size=(768, 1024)
)

print("Loaded environment:", env)
obs = env.reset()

def masked_sample(obs, action_space):
    act = action_space.sample()

    valid_types = np.flatnonzero(obs["masks"]["action_type"])
    a_type = int(np.random.choice(valid_types))
    act[5] = a_type

    if a_type == 4:  # craft
        valid_items = np.flatnonzero(obs["masks"]["craft_smelt"])
        act[6] = int(np.random.choice(valid_items)) if len(valid_items) else 0

    elif a_type == 5:  # equip
        valid_slots = np.flatnonzero(obs["masks"]["equip"])
        act[7] = int(np.random.choice(valid_slots)) if len(valid_slots) else 0

    elif a_type == 6:  # place
        valid_slots = np.flatnonzero(obs["masks"]["place"])
        act[7] = int(np.random.choice(valid_slots)) if len(valid_slots) else 0

    elif a_type == 7:  # destroy
        valid_slots = np.flatnonzero(obs["masks"]["destroy"])
        act[7] = int(np.random.choice(valid_slots)) if len(valid_slots) else 0

    else:
        act[6] = 0
        act[7] = 0

    return act

try:
    for i in range(50):
        action = masked_sample(obs, env.action_space)
        obs, reward, terminated, info = env.step(action)
        
        print(f"Step: {i}, Reward: {reward}")
        time.sleep(0.1)

        
except Exception as e:
    print("An error occurred during evaluation:", e)
finally:
    env.close()
    virtual_display.stop()
    print("Finished evaluation.")