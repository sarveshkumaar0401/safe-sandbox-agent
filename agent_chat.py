from agent_tools import agent

while True:

    prompt = input("\nYou: ")

    if prompt.lower() == "exit":
        break

    result = agent.run_sync(prompt)

    print("\nAgent:")
    print(result.output)