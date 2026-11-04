"""Proba poslužitelja: pokrene posluzitelj.py preko stdio, kao što to radi
domaćin, ispiše popis alata i pozove pronadi_materijal("A.5.3").

Pokretanje iz virtualnog okruženja s paketom mcp[cli]==2.3.0:
    python proba.py                              (osnovni poslužitelj)
    python proba.py posluzitelj_pokrivenost.py   (i drugi alat)
Ništa ne šalje na internet i ne mijenja nijednu datoteku.
"""
import asyncio
import sys
from pathlib import Path

from mcp import Client, StdioServerParameters

MAPA = Path(__file__).resolve().parent
POSLUZITELJ = MAPA / (sys.argv[1] if len(sys.argv) > 1 else "posluzitelj.py")


def tekst(rezultat):
    """Tekstni dijelovi rezultata alata, spojeni u jedan redak."""
    return " ".join(getattr(d, "text", "") for d in rezultat.content)


async def main():
    parametri = StdioServerParameters(command=sys.executable,
                                      args=[str(POSLUZITELJ)])
    async with Client(parametri) as klijent:
        alati = await klijent.list_tools()
        print("Alati:")
        for alat in alati.tools:
            print(f"  {alat.name}: {alat.description}")
        rezultat = await klijent.call_tool("pronadi_materijal", {"ishod": "A.5.3"})
        if rezultat.is_error:
            sys.exit("Alat je javio pogrešku: " + tekst(rezultat))
        nadeno = (rezultat.structured_content or {}).get("result")
        print("pronadi_materijal('A.5.3'):", nadeno if nadeno is not None
              else tekst(rezultat))
        if any(a.name == "pokrivenost" for a in alati.tools):
            pokriv = await klijent.call_tool("pokrivenost", {})
            podaci = pokriv.structured_content or {}   # rječnik: ishod -> listići
            print("pokrivenost:")
            for sifra, listici in podaci.items():
                print(f"  {sifra:8} {len(listici):3}")


if __name__ == "__main__":
    asyncio.run(main())
