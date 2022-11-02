from fastapi import FastAPI  # type: ignore
from dapr.actor.runtime.config import (
    ActorRuntimeConfig, 
    ActorTypeConfig, 
    ActorReentrancyConfig,
)
from dapr.actor.runtime.runtime import ActorRuntime
from dapr.ext.fastapi import DaprActor  # type: ignore
from fastapi import FastAPI 

from demo_actor import DemoActor


app = FastAPI(title=f'{DemoActor.__name__}Service')

# This is an optional advanced configuration which enables reentrancy only for the
# specified actor type. By default reentrancy is not enabled for all actor types.
config = ActorRuntimeConfig()  # init with default values
config.update_actor_type_configs([
    ActorTypeConfig(
        actor_type=DemoActor.__name__,
        reentrancy=ActorReentrancyConfig(enabled=True))
])
ActorRuntime.set_actor_config(config)

# Add Dapr Actor Extension
actor = DaprActor(app)


@app.on_event("startup")
async def startup_event():
    # Register DemoActor
    await actor.register_actor(DemoActor)