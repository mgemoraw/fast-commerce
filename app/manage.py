# cli.py
import typer
from typing_extensions import Annotated
from main import app as fastapi_app
import uvicorn
import os

cli = typer.Typer(
    help="A Django-like CLI for managing your FastAPI project.",
    no_args_is_help=True
)

@cli.command()
def runserver(
    host: Annotated[str, typer.Option(help="Host to run the server on")] = "127.0.0.1",
    port: Annotated[int, typer.Option(help="Port to run the server on")] = 8000,
    reload: Annotated[bool, typer.Option(help="Enable auto-reload for development")] = True,
):
    """
    Run the FastAPI development server.
    """
    typer.echo(f"Starting FastAPI server at http://{host}:{port} with reload={reload}...")
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=reload
    )

@cli.command()
def createsuperuser():
    """
    Create a superuser for the application.
    """
    typer.echo("Creating a new superuser...")
    # This is where your custom logic for creating a user would go.
    # e.g., you would interact with your database ORM here.
    # user_service.create_superuser_interactive()
    typer.echo("Superuser created successfully!")

# You can add more complex commands here, for migrations, data seeding, etc.
@cli.command()
def makemigrations():
    """
    Generates new database migration files.
    """
    typer.echo("Generating migrations...")
    # e.g., subprocess.run(["alembic", "revision", "--autogenerate", "-m", "initial migration"])
    typer.echo("Migrations generated.")

if __name__ == "__main__":
    cli()