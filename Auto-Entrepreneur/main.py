import typer
from ai import AI
from db import DB, DBs

def main(prompt: str = typer.Argument(..., help="The prompt for the AI")):
    # Initialize the AI and databases
    ai = AI()
    dbs = DBs(
        memory=DB("memory"),
        logs=DB("logs"),
        identity=DB("identity"),
        input=DB("input"),
        workspace=DB("workspace"),
    )

    # Generate a response from the AI
    response = ai.generate(prompt)

    # Save the response to the logs database
    dbs.logs["latest_response"] = response

    # Print the response
    print(response)

if __name__ == "__main__":
    typer.run(main)
