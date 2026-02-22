import tempfile
import subprocess
import sys
from pathlib import Path


def test_cli_average_gdp():
    content = """country,year,gdp,gdp_growth,inflation,unemployment,population,continent
A,2023,10,0,0,0,0,X
A,2022,20,0,0,0,0,X
B,2023,30,0,0,0,0,X
"""

    with tempfile.TemporaryDirectory() as tmp:
        file_path = Path(tmp) / "data.csv"
        file_path.write_text(content, encoding="utf-8")

        result = subprocess.run(
            [
                sys.executable,
                "main.py",
                "--files",
                str(file_path),
                "--report",
                "average-gdp",
            ],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0
        assert "A" in result.stdout
        assert "B" in result.stdout