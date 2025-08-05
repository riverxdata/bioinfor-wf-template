import pytest
import subprocess
from pathlib import Path

from apps.fastqc.main import run_fastqc


@pytest.fixture
def data_dir():
    return Path(__file__).parent / "data"


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
def test_run_fastqc_e2e(dummy_fastq_files, data_dir):
    fastq1, fastq2 = dummy_fastq_files
    output_dir = data_dir / "fastqc_results"
    run_fastqc(fastq1, fastq2, str(output_dir))
    # Check FastQC output files exist
    out_files = list(output_dir.glob("*.zip"))
    assert len(out_files) == 2
