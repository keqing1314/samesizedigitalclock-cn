#!/usr/bin/env python3
"""将 Plasma 小部件目录打包为可安装的 .plasmoid 文件。

用法::

    python3 scripts/package_plasmoid.py [输出目录]

默认输出到 ``dist/``，文件名为 ``<插件ID>-<版本>.plasmoid``。
该文件可通过 Plasma 桌面右键 →「添加小部件」→「从本地文件安装」直接安装，
也可作为 GitHub Release 的附件分发。

仅依赖 Python 3 标准库，无需安装 ``zip`` 命令。
"""

from __future__ import annotations

import json
import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
# .plasmoid 包内需要包含的顶层条目
PACKAGE_ENTRIES = ("metadata.json", "contents")


def read_metadata() -> tuple[str, str]:
    """读取插件 ID 与版本号。"""
    metadata_path = REPO_ROOT / "metadata.json"
    with metadata_path.open(encoding="utf-8") as fh:
        metadata = json.load(fh)

    plugin = metadata.get("KPlugin")
    if not isinstance(plugin, dict):
        raise SystemExit("错误：metadata.json 中缺少 KPlugin 段")

    plugin_id = plugin.get("Id")
    if not plugin_id:
        raise SystemExit("错误：metadata.json 中缺少 KPlugin.Id")

    version = plugin.get("Version", "0.0.0")
    return plugin_id, version


def collect_files() -> list[Path]:
    """收集需要打包的文件（保持相对仓库根的路径）。"""
    files: list[Path] = []
    for entry in PACKAGE_ENTRIES:
        target = REPO_ROOT / entry
        if not target.exists():
            raise SystemExit(f"错误：未找到 {entry}")
        if target.is_file():
            files.append(target)
        else:
            files.extend(sorted(p for p in target.rglob("*") if p.is_file()))
    return files


def build(output_dir: Path, plugin_id: str, version: str) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    artifact = output_dir / f"{plugin_id}-{version}.plasmoid"

    with zipfile.ZipFile(artifact, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in collect_files():
            # 包内结构：<插件ID>/metadata.json、<插件ID>/contents/...
            arcname = f"{plugin_id}/{path.relative_to(REPO_ROOT).as_posix()}"
            archive.write(path, arcname)

    return artifact


def main(argv: list[str]) -> int:
    output_dir = Path(argv[1]) if len(argv) > 1 else REPO_ROOT / "dist"
    if not output_dir.is_absolute():
        output_dir = REPO_ROOT / output_dir

    plugin_id, version = read_metadata()
    artifact = build(output_dir, plugin_id, version)

    with zipfile.ZipFile(artifact) as archive:
        entries = archive.namelist()

    print(f"插件 ID : {plugin_id}")
    print(f"版本    : {version}")
    print(f"输出    : {artifact}")
    print(f"文件数  : {len(entries)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
