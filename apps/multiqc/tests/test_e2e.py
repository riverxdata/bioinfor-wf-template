import pytest
import subprocess
from pathlib import Path

from apps.multiqc.main import run_multiqc


@pytest.fixture
def data_dir():
    return Path(__file__).parent / "data"


@pytest.mark.skipif(
    not (subprocess.run(["docker", "--version"], capture_output=True).returncode == 0),
    reason="Docker is not available",
)
def test_run_multiqc_e2e(data_dir):
    multiqc_dir = data_dir / "multiqc_results"
    fastqc_dir = data_dir / "fastqc_results"
    run_multiqc(fastqc_dir, str(multiqc_dir))
