import cyclopts

app = cyclopts.App(name="pathex", help="Clinical pathology entity extraction tool")


@app.default
def main() -> None:
    """Main entry point for pathex CLI."""
    print("Hello from pathex!")
