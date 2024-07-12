from crewai import Task
from crewai_tools import PDFSearchTool, ScrapeWebsiteTool, SeleniumScrapingTool, SerperDevTool, TXTSearchTool, YoutubeVideoSearchTool, WebsiteSearchTool
from dotenv import load_dotenv

load_dotenv()


class creatorTasks:
    def research_task(self, agent, user_case):
        pdf_tool = PDFSearchTool()
        scrape_tool = ScrapeWebsiteTool()
        selenium_tool = SeleniumScrapingTool()
        serper_tool = SerperDevTool()
        txt_tool = TXTSearchTool()
        youtube_tool = YoutubeVideoSearchTool()
        website_tool = WebsiteSearchTool()
        
        
        return Task(
            description=(
                f"Find all the relevant research on how to build a really strong agent from CrewAi's framework that is the best use for {user_case}. "
                "Gather information on how it works and the best practices for coding the agent. Use all the provided tools to find the best and most recent research regarding CrewAI agent building and coding."
            ),
            expected_output="A comprehensive collection of research findings related to CrewAI agent building and coding.",
            tools=[
                pdf_tool, scrape_tool, selenium_tool, serper_tool, txt_tool, youtube_tool, website_tool
            ],
            agent=agent,
        )

    def compile_research_task(self, agent, user_case):

        
        return Task(
            description=(
                f"Take in all the research provided by the agent_researcher and compile it into the CrewAI format for {user_case}. "
                "Generate all the agent attributes including role, goal, backstory, max_iter, max_rpm, max_execution_time, verbose, allow_delegation, step_callback, and cache. "
                f"Only include optional attributes if necessary based on {user_case}."
            ),
            expected_output="A detailed compilation of agent attributes in text form based on the provided research.",
            agent=agent,
        )

    def code_generation_task(self, agent, user_case):        
        return Task(
            description=(
                "Convert the text output from the research_compiler_agent into functional code that defines an Agent in the CrewAI framework. "
                f"Consider the specific requirements and nuances of {user_case} to ensure the resulting code is both efficient and effective. "
                "The final output should be a complete and executable Python block of code that accurately represents the agent's attributes and functionalities."
            ),
            expected_output=(
                "An executable Python block of code that defines an Agent in the CrewAI framework based on the provided text."
                "EXAMPLE OUTPUT"
                "def AGENT_NAME(self, OTHER_VARIABLES)"
                    "return Agent("
                        "role='Data Analyst',"
                        "goal='Extract actionable insights',"
                        "backstory='You're a data analyst at a large company'."
                        "You're responsible for analyzing data and providing insights to the business."
                        "You're currently working on a project to analyze the performance of our marketing campaigns."
                        'tools=[my_tool1, my_tool2],  # Optional, defaults to an empty list'
                        'llm=my_llm,  # Optional'
                        'function_calling_llm=my_llm,  # Optional'
                        'max_iter=15,  # Optional'
                        'max_rpm=None, # Optional'
                        'verbose=True,  # Optional'
                        'allow_delegation=True,  # Optional'
                        'step_callback=my_intermediate_step_callback,  # Optional'
                        'cache=True  # Optional'
                    ")"
                    
                "DO NOT inlcude any other information besides the blocks of code for the Agent described in the EXAMPLE OUTPUT"
                "Any other code you provide is irrelavent to the user, all they want is just the example block you have been provided"
                    
            ), 
            agent=agent,
        )

    def code_review_task(self, agent, user_case):        
        return Task(
            description=(
                f"Review and simplify the CrewAI agent code for {user_case}. Ensure it's a minimal, functional definition with only essential components. The final output should be a clean Python code block defining just the basic agent."
            ),
            expected_output=(
                f"A refined and polished Python code block that is functional, efficient, and optimized for the specific requirements of {user_case}."
                "EXAMPLE OUTPUT"
                "def AGENT_NAME(self, OTHER_VARIABLES)"
                    "return Agent("
                        "role='Data Analyst',"
                        "goal='Extract actionable insights',"
                        "backstory=('You're a data analyst at a large company'."
                        "You're responsible for analyzing data and providing insights to the business."
                        "You're currently working on a project to analyze the performance of our marketing campaigns.')"
                        'tools=[my_tool1, my_tool2],  # Optional, defaults to an empty list'
                        'llm=my_llm,  # Optional'
                        'max_iter=15,  # Optional'
                        'max_rpm=None, # Optional'
                        'verbose=True,  # Optional'
                        'allow_delegation=True,  # Optional'
                        'cache=True  # Optional'
                    ")"
                
                f"MAKE SURE that if any variables are set in the goal or backstory within curley brackets, they are also included in the parameters of the function!"
                    
                "DO NOT inlcude any other information besides the blocks of code for the Agent described in the EXAMPLE OUTPUT"
                "Any other code you provide is irrelavent to the user, all they want is just the example block you have been provided"
            ),
            agent=agent,
        )
