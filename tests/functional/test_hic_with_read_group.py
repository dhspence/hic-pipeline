from pathlib import Path

import pysam
import pytest


@pytest.mark.workflow("test_hic_with_read_group")
def test_read_group_added_to_bam_header(workflow_dir):
    bam_path = workflow_dir / Path("test-output/with_read_group.bam")
    with pysam.AlignmentFile(str(bam_path)) as bam:
        assert bam.header.get("RG")[0]["ID"] == "foo"


@pytest.mark.workflow("test_hic_with_read_group")
def test_hic_with_read_group_alignable_bam_match(workflow_dir, bam_md5):
    bam_path = workflow_dir / Path("test-output/result_alignable_dedup.bam")
    bam_md5sum = bam_md5(bam_path)
    assert bam_md5sum == "2ab25d2ce156837a5d10ffa8a2a293c2"


@pytest.mark.workflow("test_hic_with_read_group")
def test_hic_with_read_group_pairs_match(workflow_dir, skip_n_lines_md5):
    pairs_path = workflow_dir / Path("test-output/pairix.bsorted.pairs.gz")
    pairs_md5 = skip_n_lines_md5(pairs_path, n_lines=5)
    assert pairs_md5 == "a95ca169256c73b02f2c347b85b41215"
