import pytest
from apps.fastqc.main import validate_fastq_files


def test_validate_fastq_files_valid_pair():
    fastq1 = "/path/sample_R1_001.fastq.gz"
    fastq2 = "/path/sample_R2_001.fastq.gz"
    # Should not raise
    validate_fastq_files(fastq1, fastq2)


def test_validate_fastq_files_invalid_pair():
    fastq1 = "/path/sample_R1_001.fastq.gz"
    fastq2 = "/path/sample_R3_001.fastq.gz"
    with pytest.raises(ValueError):
        validate_fastq_files(fastq1, fastq2)


def test_validate_fastq_files_no_r1_in_name():
    fastq1 = "/path/sample_001.fastq.gz"
    fastq2 = "/path/sample_001.fastq.gz"
    # Should not raise, as _R1_ is not present, so nothing is replaced
    validate_fastq_files(fastq1, fastq2)


def test_validate_fastq_files_partial_match():
    fastq1 = "/path/sample_R1_001.fastq.gz"
    fastq2 = "/path/sample_R2_002.fastq.gz"
    with pytest.raises(ValueError):
        validate_fastq_files(fastq1, fastq2)


def test_validate_fastq_files_different_extensions():
    fastq1 = "/path/sample_R1_001.fq"
    fastq2 = "/path/sample_R2_001.fq"
    validate_fastq_files(fastq1, fastq2)


def test_validate_fastq_files_subdir():
    fastq1 = "/data/reads/sample_R1_001.fastq.gz"
    fastq2 = "/other/sample_R2_001.fastq.gz"
    validate_fastq_files(fastq1, fastq2)
