# 2025-08-21 Thursday 17:53:35.
import os
import re
from datetime import datetime
from pathlib import Path

import pypandoc


def modify_headings(content, heading_replacements):
    if not heading_replacements:
        return content

    modified_content = content
    for old_heading, new_heading in heading_replacements.items():
        modified_content = re.sub(re.escape(old_heading), new_heading, modified_content)
    return modified_content


def main():
    # ===========================================================
    current_file = os.path.abspath(__file__)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    full_path = os.path.join(dir_path, current_file)
    print(f"Current file: {full_path}")
    now = datetime.today().strftime("%Y-%m-%d %a. %#I:%M:%S %p")
    start_time = datetime.now()
    print(f"Current time: {now}\n")
    print("===================\n")
    # ===========================================================

    purl_specification_input = [
        "docs-md-2025-08-21/standard/header.md",
        "docs-md-2025-08-21/purl-spec-toc.md",
        "docs-md-2025-08-21/standard/specification-summary.md",
        "docs-md-2025-08-21/examples.md",
        "docs-md-2025-08-21/standard/components.md",
        "docs-md-2025-08-21/standard/characters-and-encoding.md",
        "docs-md-2025-08-21/how-to-build.md",
        "docs-md-2025-08-21/how-to-parse.md",
        "docs-md-2025-08-21/known-qualifiers.md",
        "docs-md-2025-08-21/tests.md",
    ]

    purl_standard_input = [
        "docs-md-2025-08-21/standard/header.md",
        "docs-md-2025-08-21/standard/about.md",
        "docs-md-2025-08-21/standard/introduction.md",
        "docs-md-2025-08-21/standard/conformance.md",
        "docs-md-2025-08-21/standard/references.md",
        "docs-md-2025-08-21/standard/overview.md",
        "docs-md-2025-08-21/standard/summary.md",
        "docs-md-2025-08-21/standard/characters-and-encoding.md",
        "docs-md-2025-08-21/standard/components.md",
        "docs-md-2025-08-21/standard/types.md",
        "docs-md-2025-08-21/standard/annex-a.md",
    ]

    heading_modifications = {
        "docs-md-2025-08-21/standard/summary.md": {
            "## What is a `purl`?": "# 5 Package-URL Specification",
        },
        "docs-md-2025-08-21/standard/characters-and-encoding.md": {
            "## Permitted characters": "## 5.1 Permitted Characters",
            "## Separators": "## 5.2 Separator Characters",
            "## Character encoding": "## 5.3 Character Encoding",
            "## Case folding": "## 5.4 Case Folding",
        },
        "docs-md-2025-08-21/standard/components.md": {
            "## Rules for each `purl` component": "## 5.5 Component-level Rules"
        },
        "docs-md-2025-08-21/standard/types.md": {
            "## Package-URL Type definitions": "## 5.6 PURL Types"
        },
    }

    combined_parts = []

    # Choose which output.md we want:
    # input_list = purl_specification_input
    input_list = purl_standard_input

    for filename in input_list:
        path = Path(filename)

        if not path.exists():
            raise FileNotFoundError(f"Input file not found: {filename}")

        content = path.read_text(encoding="utf-8")

        # Check if this file needs heading modifications
        if input_list == purl_standard_input and filename in heading_modifications:
            content = modify_headings(content, heading_modifications[filename])
            print(f"Applied heading modifications to: {filename}")

        combined_parts.append(content)

    combined_md = "\n\n".join(combined_parts)

    # output_dir = Path("../output-md-2025-08-20-01")
    output_dir = Path("output-md-2025-08-21")
    output_dir.mkdir(parents=True, exist_ok=True)

    if input_list == purl_specification_input:
        output_path = output_dir / "purl-specification.md"
    else:
        output_path = output_dir / "purl-standard.md"

    # Convert combined markdown text to markdown file (via pandoc)
    pypandoc.convert_text(
        combined_md,
        "gfm",  # GFM output format
        format="markdown",  # input format
        outputfile=str(output_path),
        extra_args=["--standalone"],
    )

    # ==========================================================================
    nownow = datetime.today().strftime("%Y-%m-%d %a. %#I:%M:%S %p")
    print(f"✅ {now} -- Output sent to \n\n\t{output_path}")
    # ===========================================================
    print("\n===================\n")
    print(f"Current time: {now}")
    time_elapsed = datetime.now() - start_time
    print("Time elapsed (hh:mm:ss.ms) {}".format(time_elapsed))
    print("datetime.now() = {}\n".format(datetime.now()))
    # ===========================================================


if __name__ == "__main__":
    main()



# ====================================
# def main():
#     # your existing logic goes here
#     print(f"\nAssembling docs...\n")

# if __name__ == "__main__":
#     main()
