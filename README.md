# AI Agent Creator

This project utilizes the CrewAI framework to automatically generate custom CrewAI AI agents based on user specifications. It leverages a team of specialized AI agents to research, compile, code, and refine the creation of a new CrewAI AI agent tailored to the user's needs.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [File Structure](#file-structure)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automated research on CrewAI framework and best practices
- Compilation of research into actionable agent attributes
- Generation of functional Python code for the custom agent
- Code review and optimization
- Flexible and extensible architecture

## Requirements

- Python 3.7+
- CrewAI library
- Anthropic API key
- Serper API key
- OpenAI API key (optional, for GPT model usage)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/bosmanbos/ai-agent-creator.git
   cd ai-agent-creator
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your API keys:
   - Create a `.env` file in the project root
   - Add your API keys:
     ```
     OPENAI_API_KEY=your_openai_api_key
     SERPER_API_KEY=your_serper_api_key
     ANTHROPIC_API_KEY=your_anthropic_api_key
     ```

## Usage

1. Run the main script:
   ```
   python ./src/agent_creator/main.py
   ```

2. Follow the prompts to specify your desired agent functionality.

3. The program will generate a custom AI agent based on your input and save it to `Your_Agent.txt`.

## Architecture

The AI Agent Creator consists of four specialized agents:

1. **Agent Researcher**: Gathers relevant information on building strong agents using the CrewAI framework.
2. **Research Compiler**: Synthesizes the research into a structured format suitable for agent creation.
3. **Coding Specialist**: Transforms the compiled research into functional Python code defining the new agent.
4. **Code Editor**: Reviews and optimizes the generated code for efficiency and readability.

These agents work sequentially in a crew, each building upon the output of the previous one.

## File Structure

- `main.py`: Entry point of the application
- `Agents_and_Tasks.py`: Defines the specialized agents and their tasks
- `Your_Agent.txt`: Output file containing the generated agent code
- `requirements.txt`: List of Python dependencies
- `.env`: (Create this file) Stores API keys and other environment variables

## Customization

You can customize the behavior of the AI Agent Creator by modifying the following:

- `Agents_and_Tasks.py`: Adjust agent roles, goals, and backstories
- `main.py`: Modify the crew setup or process flow
- Add new tools or integrate additional APIs in the `creatorAgents` class

## Troubleshooting

- **API Key Issues**: Ensure all required API keys are correctly set in your `.env` file or environment variables.
- **Dependency Errors**: Make sure all dependencies are installed using `pip install -r requirements.txt`.
- **Output Errors**: Check the console output for any error messages. The verbose mode in the crew setup can provide more detailed information about the process.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.


## License

This project is open source and available under the [MIT License](LICENSE).
