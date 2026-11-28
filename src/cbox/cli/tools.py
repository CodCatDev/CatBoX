import platform
from ..config import BuildInfo, Magic
from datetime import datetime


class Tools:
    @classmethod
    def info(cls) -> str:
        host = f"{platform.python_implementation()} {platform.python_version()}"
        if platform.system().lower() in ["linux"]:
            distr = platform.freedesktop_os_release()
            version = platform.release().split("-")[0]
            osVersion = f"{distr.get("NAME", "Linux")} {version} ({platform.machine()})"
        else:
            osVersion = f"{platform.system()} {platform.release()} ({platform.machine()})"

        return f"""
   /\\___/\\      cbox {BuildInfo.Version}-{BuildInfo.Branch} (b{BuildInfo.Build})
  (  o.o  )     ────────────────────────────────────
   >  ^  <      Author:   CodCatDev
  ┌───────┐     License:  MIT
  │ CBOX  │     Repo:     https://github.com/codcatdev/catbox
  └───────┘     Format:   .cbox (spec {BuildInfo.FormatSpec}, magic: {Magic.Text} ({Magic.Hex}))
                Codecs:   No
                Checksum: No
                Runtime:  {host}
                OS:       {osVersion}

        """.lstrip('\n').rstrip()

    @classmethod
    def version(cls) -> str:
        year = datetime.now().year
        copyrightYear = "2026" if year == 2026 else f"2026-{year}"
        return f"cbox v{BuildInfo.Version}-{BuildInfo.Branch} b{BuildInfo.Build} (format spec {BuildInfo.FormatSpec}, {platform.system().lower()}/{platform.machine()})\n" \
                f"copyright (c) CodCatDev {copyrightYear}, MIT License\n" \
                "repo https://github.com/codcatdev/catbox"