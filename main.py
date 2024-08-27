import typer
import pymupdf
from pathlib import Path
from more_itertools import flatten
from typing_extensions import Annotated


def main(
    files: Annotated[str, typer.Option(help="Comma separated list of files")] = None,
    extension: Annotated[str, typer.Option(help="Comma separated Extension of the files")] = "tif",
    filename: Annotated[str, typer.Option(help="Name of the output file")] = "output.pdf",
):
    """
    Convert a list of images to a PDF file.
    """
    doc = pymupdf.Document()
    typer.echo(f"Looking for files with extension: *.{extension}")
    files_ = files and files.split(",")
    if not files_:
        current_dir = Path(".")
        files_ = list(flatten([current_dir.glob(f"*.{ext}") for ext in extension.split(",")]))
    typer.echo(f"Files found: {files_}")
    if not files_:
        typer.echo("No files found.")
        raise typer.Exit()
    for i in files_:
        print(i)
        pixmap = pymupdf.Pixmap(i)
        doc.insert_file(pixmap)
    typer.echo(f"Saving to {filename}")
    doc.save(filename=filename)
    doc.close()


typer.run(main)
