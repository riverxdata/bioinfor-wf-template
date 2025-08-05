import subprocess
import os


def validate_fastq_files(fastq1: str, fastq2: str):
    """
    Validate that fastq2 filename matches fastq1 with _R1_ replaced by _R2_.

    Args:
        fastq1 (str): Path to first FASTQ file.
        fastq2 (str): Path to second FASTQ file.

    Raises:
        ValueError: If fastq2 filename does not match fastq1 with _R1_ replaced by _R2_.
    """
    base1 = os.path.basename(fastq1)
    base2 = os.path.basename(fastq2)
    expected_base2 = base1.replace("_R1_", "_R2_")
    if base2 != expected_base2:
        raise ValueError(
            f"FASTQ file names do not match: expected '{expected_base2}' for read 2, got '{base2}'"
        )


def run_fastqc(
    fastq1: str,
    fastq2: str,
    output_dir: str,
):
    """
    Run FastQC on paired FASTQ files using Docker.

    Args:
        fastq1 (str): Path to first FASTQ file.
        fastq2 (str): Path to second FASTQ file.
        output_dir (str): Directory to store FastQC results.
        fastqc_version (str): FastQC Docker image version (default: '0.12.1').
    """
    os.makedirs(output_dir, exist_ok=True)
    cwd = os.path.abspath(os.getcwd())
    fastq1_abs = os.path.abspath(fastq1)
    fastq2_abs = os.path.abspath(fastq2)
    validate_fastq_files(fastq1_abs, fastq2_abs)
    output_dir_abs = os.path.abspath(output_dir)

    cmd = [
        "docker",
        "run",
        "--rm",
        "-v",
        f"{cwd}:{cwd}",
        "-w",
        cwd,
        "biocontainers/fastqc:v0.11.9_cv8",
        "fastqc",
        fastq1_abs,
        fastq2_abs,
        "--outdir",
        output_dir_abs,
    ]
    subprocess.run(cmd, check=True)
