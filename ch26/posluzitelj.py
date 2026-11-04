from pathlib import Path
from mcp.server import MCPServer

# POSTAVKE: jedina mapa koju poslužitelj smije čitati
# U repozitoriju je to izmišljena mapa pokraj ove datoteke; svoju upišite
# potpunom putanjom, npr. Path("/Users/tomislav/knjiznica").
MAPA = Path(__file__).resolve().parent / "knjiznica"
mcp = MCPServer("Knjižnica 5. razred")

@mcp.resource("ishodi://matematika-5", mime_type="text/markdown")
def ishodi() -> str:
    """Ishodi Matematike za 5. razred, prepisani iz kurikula."""
    return (MAPA / "ishodi.md").read_text(encoding="utf-8")

@mcp.prompt(title="Radni listić")
def radni_listic(tema: str, razred: str = "5.") -> str:
    """Provjereni upit za radni listić iz knjižnice upita."""
    upit = (MAPA / "upiti" / "listic.md").read_text(encoding="utf-8")
    return upit.replace("[TEMA]", tema).replace("[RAZRED]", razred)

@mcp.tool()
def pronadi_materijal(ishod: str) -> list[str]:
    """Listići označeni ishodom, npr. 'A.5.3'. Samo čita mapu."""
    nadeno = []
    for listic in sorted((MAPA / "listici").glob("*.md")):
        oznake = listic.read_text(encoding="utf-8").splitlines()[0]
        if ishod in oznake:
            nadeno.append(listic.stem)
    return nadeno

if __name__ == "__main__":
    mcp.run()                                 # bez argumenta: stdio
