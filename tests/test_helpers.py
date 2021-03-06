#!/usr/bin/env python3

"""
Test suite for classes
"""

from pathlib import Path

import io
import shutil

import pytest
import pytest_mock

import requests
import requests_mock

from cblaster import helpers


TEST_DIR = Path(__file__).resolve().parent


def test_efetch_sequences(monkeypatch):
    def mock_sequences(*args, **kwargs):
        return io.StringIO(">seq1\nABC\n>seq2\nDEF\n>seq3\nGHI")
    from Bio import Entrez
    monkeypatch.setattr(Entrez, "efetch", mock_sequences)
    assert helpers.efetch_sequences(["seq1", "seq2", "seq3"]) == {
        "seq1": "ABC",
        "seq2": "DEF",
        "seq3": "GHI",
    }
    return


def test_efetch_sequences_IOError(monkeypatch):
    def mock_ioerror(*args, **kwargs):
        raise IOError
    from Bio import Entrez
    monkeypatch.setattr(Entrez, "efetch", mock_ioerror)
    with pytest.raises(IOError):
        helpers.efetch_sequences(["seq"])


def test_get_sequences_query_file(mocker):
    sequences = helpers.get_sequences(query_file=TEST_DIR / "test.faa")
    assert {'QBE85648.1', 'QBE85647.1', 'QBE85646.1'}.issubset(sequences)


def test_get_sequences_query_ids(mocker):
    mocker.patch("cblaster.helpers.efetch_sequences")
    helpers.get_sequences(query_ids=["seq1", "seq2"])
    helpers.efetch_sequences.assert_called_once_with(["seq1", "seq2"])


def test_get_sequences_bad_input():
    with pytest.raises(ValueError):
        helpers.get_sequences()


def test_get_program_path_not_found(monkeypatch):
    def return_none(alias):
        return

    monkeypatch.setattr(shutil, "which", return_none)

    with pytest.raises(ValueError):
        helpers.get_program_path(["alias"])


def test_get_program_path(monkeypatch):
    def return_path(alias):
        return "test_path"

    monkeypatch.setattr(shutil, "which", return_path)

    assert helpers.get_program_path(["alias"]) == "test_path"
