import subprocess
import os


def run_multiqc(output_dir, report_dir):
    """
    Run MultiQC on FastQC results using Docker.

    Args:
        output_dir (str): Directory containing FastQC results.
        report_dir (str): Directory to store MultiQC report.
    """
    os.makedirs(report_dir, exist_ok=True)
    cwd = os.path.abspath(os.getcwd())
    output_dir_abs = os.path.abspath(output_dir)
    report_dir_abs = os.path.abspath(report_dir)

    cmd = [
        "docker",
        "run",
        "--rm",
        "-v",
        f"{cwd}:{cwd}",
        "-w",
        cwd,
        "ewels/multiqc:v1.13",
        output_dir_abs,
        "-o",
        report_dir_abs,
    ]
    subprocess.run(cmd, check=True)
