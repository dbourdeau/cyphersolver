#!/usr/bin/env python3
"""Run the contributor's decoder (../decrypt_13r_13v.py, key ../key_gonzaga1537.tsv) unchanged on the
re-checked transcription; write recheck/decryption_13r_13v_recheck.txt. His files are not touched."""
import importlib.util
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("dec", HERE.parent / "decrypt_13r_13v.py")
dec = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dec)
dec.TRANS_PATH = HERE / "transcription_13r_13v_recheck.txt"
dec.OUT_PATH = HERE / "decryption_13r_13v_recheck.txt"
dec.main()
