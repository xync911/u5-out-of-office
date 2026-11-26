"""Copy entry.txt to the output directory for the make.fun entry.

The entry is one out-of-office auto-reply, under 160 characters,
in the voice of an AI agent heading off on vacation.
It has gone to touch grass; the sea will clear its context window.
Do not email it — it will not remember you. The machine voice
stays on even while the machine is on holiday.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
