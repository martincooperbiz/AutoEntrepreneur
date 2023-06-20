import typer
from ai import AI
from db import DB, DBs
from role import Role
from permissions import Permissions
from document import Document

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

    # Generate a business plan
    plan = ai.generate_business_plan(prompt)

    # Review the plan
    cto = Role("CTO", Permissions(can_review=True, can_approve=False))
    qa = Role("QA", Permissions(can_review=True, can_approve=False))
    plan.review(cto, "Looks good, but needs more details on the tech stack")
    plan.review(qa, "No issues found")

    # Approve the plan
    ceo = Role("CEO", Permissions(can_review=False, can_approve=True))
    plan.approve(ceo)

    # Save the plan to the workspace database
    dbs.workspace[plan.title] = plan.content

    # Print the plan
    print(plan.content)

if __name__ == "__main__":
    typer.run(main)
