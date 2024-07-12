import os
from crewai import Crew, Process
from textwrap import dedent
from Agents import creatorAgents
from Tasks import creatorTasks
from dotenv import load_dotenv
import re

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")
anthropic_api_key = os.getenv("ANTRHOPIC_API_KEY")


class agentCrew:
    
    def __init__(self, user_case):
        self.user_case = user_case
        
    def run(self):
        agents = creatorAgents()
        tasks = creatorTasks()
        
        agent_researcher_agent = agents.agent_researcher_agent(user_case)
        research_compiler_agent = agents.research_compiler_agent(user_case)
        coding_specialist = agents.coding_specialist(user_case)
        code_editor = agents.code_editor(user_case)
        
        research_task = tasks.research_task(
            agent_researcher_agent,
            self.user_case,
        )
        
        compile_research_task = tasks.compile_research_task(
            research_compiler_agent,
            self.user_case,
        )
        
        code_generation_task = tasks.code_generation_task(
            coding_specialist,
            self.user_case,
        )
        
        code_review_task = tasks.code_review_task(
            code_editor,
            self.user_case,
        )
        
        
        crew = Crew(
            agents=[
                agent_researcher_agent, research_compiler_agent, coding_specialist, code_editor
            ],
            tasks=[
                research_task, compile_research_task, code_generation_task, code_review_task
            ],
            verbose=True,
            memory = True,
            process=Process.sequential
        )
        
        result = crew.kickoff()
        return filter_agent_def(result)
        


def filter_agent_def(result):
    pattern = r'def\s+\w+\s*\([^)]*\):\s*\n\s*return\s+Agent\([\s\S]+?\n\s*\)'
    matches = re.findall(pattern, result, re.DOTALL)
    filtered_result = '\n\n'.join(matches)
    return filtered_result



if __name__ == "__main__":
    print("### Welcome to your AI agent creator ###")
    print("----------------------------------------")
        
    user_case = input(
        dedent("""
            What would you like you agent to do?
        """)
    )
    
    agent_crew = agentCrew(user_case)
    result = agent_crew.run()
        
    output_file = "Your_Agent.txt"
    with open(output_file, 'w') as f:
        f.write(result)
        
    
    print("\n\n########################################")
    print("     ### Here is your agent ###")
    print("########################################\n\n")
    print(f"Final Result: {result}")
    print("\n\n")
