from pathlib import Path

import pysam
import pytest


@pytest.fixture
def bam_path(workflow_dir):
    return workflow_dir / Path("test-output/with_read_group.bam")


@pytest.mark.workflow("test_add_read_group_to_bam")
def test_add_read_group_to_bam_read_group_added_to_bam_header(workflow_dir, bam_path):
    with pysam.AlignmentFile(str(bam_path)) as bam:
        assert bam.header.get("RG")[0]["ID"] == "foo"
        assert bam.header.get("RG")[0]["DS"] == "cool"


@pytest.mark.workflow("test_add_read_group_to_bam")
def test_add_read_group_to_bam_bam_match(workflow_dir, bam_path, bam_md5):
    bam_md5sum = bam_md5(bam_path)
    assert bam_md5sum == "8cb6f293859775fdee81a51c73f51c1e"
