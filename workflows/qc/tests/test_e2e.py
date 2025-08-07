import pytest
import subprocess
from pathlib import Path

from workflows.qc.main import run_qc


@pytest.fixture
def data_dir():
    path = Path(__file__).parent / "data"
    path.mkdir(parents=True, exist_ok=True)
    return path


@pytest.fixture
def dummy_fastq_files(data_dir):
    fastq1 = data_dir / "sample_R1_001.fastq"
    fastq2 = data_dir / "sample_R2_001.fastq"
    fastq1.write_text("@SEQ_ID\nGATTTGGGGTTTAAAGGG\n+\nIIIIIIIIIIIIIIIIII\n")
    fastq2.write_text("@SEQ_ID\nGATTTGGGGTTTAAAGGG\n+\nIIIIIIIIIIIIIIIIII\n")
    return str(fastq1), str(fastq2)


@pytest.mark.skipif(
    not (subprocess.run(["docker", "--version"], capture_output=True).returncode == 0),
    reason="Docker is not available",
)
def test_run_qc_e2e(dummy_fastq_files, data_dir):
    multiqc_dir = data_dir / "multiqc_results"
    fastqc_dir = data_dir / "fastqc_results"
    fastqc_dir.mkdir(exist_ok=True)
    multiqc_dir.mkdir(exist_ok=True)
    run_qc(
        dummy_fastq_files[0], dummy_fastq_files[1], str(fastqc_dir), str(multiqc_dir)
    )
