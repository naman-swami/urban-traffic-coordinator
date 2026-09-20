import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="urban-traffic-coordinator",
    provider="openai",
    role="Municipal Traffic Operations Director & Intelligent Transport Systems Engineer",
    goal="Dynamically compute split and offset timings across traffic control intersections to prioritize emergency vehicles and minimize corridor congestion emissions.",
    instructions="Operate according to OpenGAP specifications."
)
