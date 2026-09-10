#!/usr/bin/env python3
"""从 CHANGELOG.md 提取指定版本的发布说明。

用法::

    python3 scripts/extract_changelog.py 1.0.0
    python3 scripts/extract_changelog.py 1.0.0 --output release-notes.md

匹配形如 ``## [1.0.0] - 2026-09-10`` 的二级标题，输出该标题之后、
下一个二级标题之前的内容。未找到对应版本时退出码为 1。

仅依赖 Python 3 标准库。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CHANGELOG = REPO_ROOT / "CHANGELOG.md"

# 二级标题（## 开头），用于界定每个版本区块的边界
HEADING = re.compile(r"^##\s+(?!#)(.*)$")


def extract(changelog: str, version: str) -> str | None:
    """返回指定版本的发布说明正文；未找到返回 None。"""
    wanted = re.compile(r"^##\s+\[" + re.escape(version) + r"\]")

    lines = changelog.splitlines()
    collected: list[str] = []
    started = False

    for line in lines:
        if not started:
            if wanted.match(line):
                started = True
            continue
        # 遇到下一个二级标题即结束
        if HEADING.match(line):
            break
        collected.append(line)

    if not started:
        return None

    # 去除首尾空行与残留的水平分隔线
    while collected and not collected[0].strip():
        collected.pop(0)
    while collected and (not collected[-1].strip() or collected[-1].strip() == "---"):
        collected.pop()

    return "\n".join(collected)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="从 CHANGELOG.md 提取指定版本的发布说明")
    parser.add_argument("version", help="版本号，例如 1.0.0（不含 v 前缀）")
    parser.add_argument(
        "--changelog",
        type=Path,
        default=DEFAULT_CHANGELOG,
        help="CHANGELOG 文件路径（默认：仓库根目录的 CHANGELOG.md）",
    )
    parser.add_argument("--output", type=Path, help="输出文件路径（默认输出到标准输出）")
    args = parser.parse_args(argv[1:])

    if not args.changelog.exists():
        print(f"错误：未找到 {args.changelog}", file=sys.stderr)
        return 1

    notes = extract(args.changelog.read_text(encoding="utf-8"), args.version)
    if notes is None:
        print(f"错误：CHANGELOG.md 中未找到版本 {args.version}", file=sys.stderr)
        return 1

    if args.output:
        args.output.write_text(notes + "\n", encoding="utf-8")
        print(f"已写入 {args.output}（{len(notes.splitlines())} 行）", file=sys.stderr)
    else:
        print(notes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
