from animalai.envs.arena_config import ArenaConfig

from animalai_train.run_options_aai import RunOptionsAAI
from animalai_train.run_training_aai import run_training_aai

trainer_config_path = (
    "train_mlagents_config_ppo.yaml"
)
environment_path = "env/AnimalAI"
arena_config_path = "train_mlagents_arenas.yml"
run_id = "train_ml_agents"
base_port = 5005
number_of_environments = 1
number_of_arenas_per_environment = 8

args = RunOptionsAAI(
    trainer_config=trainer_config_path,
    env_path=environment_path,
    run_id=run_id,
    base_port=base_port,
    num_envs=number_of_environments,
    arena_config=ArenaConfig(arena_config_path),
    n_arenas_per_env=number_of_arenas_per_environment,
)

mlagents-learn <trainer-config-file> --env=<env_name> --run-id=<run-identifier>