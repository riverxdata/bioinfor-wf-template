import argparse
from apps.fastqc.main import run_fastqc
from apps.multiqc.main import run_multiqc


def run_qc(fastq1, fastq2, output_dir, report_dir):
    """
    Run FastQC and MultiQC on the provided FASTQ files.

    Args:
        fastq1 (str): Path to the first FASTQ file.
        fastq2 (str): Path to the second FASTQ file.
        output_dir (str): Directory to store FastQC results.
        report_dir (str): Directory to store MultiQC report.
    """
    run_fastqc(fastq1, fastq2, output_dir)
    run_multiqc(output_dir, report_dir)
    print(f"FastQC results stored in: {output_dir}")
    print(f"MultiQC report stored in: {report_dir}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Run FastQC and MultiQC on FASTQ files."
    )
    parser.add_argument("fastq1", type=str, help="Path to the first FASTQ file.")
    parser.add_argument("fastq2", type=str, help="Path to the second FASTQ file.")
    parser.add_argument(
        "output_dir", type=str, help="Directory to store FastQC results."
    )
    parser.add_argument(
        "report_dir", type=str, help="Directory to store MultiQC report."
    )

    args = parser.parse_args()

    run_qc(args.fastq1, args.fastq2, args.output_dir, args.report_dir)
