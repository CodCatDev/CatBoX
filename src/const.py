from platform import system, machine, release, freedesktop_os_release, python_implementation, python_version

Version = "0.2.2"
Build = "1"
Branch = "dev"
Host = f"{python_implementation()} {python_version()}"
if system().lower() in ["linux"]:
    distr = freedesktop_os_release()
    version = release().split("-")[0]
    OsVersion = f"{distr.get("NAME", "Linux")} {version} ({machine()})"
else:
    OsVersion = f"{system()} {release()} ({machine()})"

VersionInfo = f"""
   /\\___/\\      cbx {Version}-{Branch} (b{Build})
  (  o.o  )     ────────────────────────────────────
   >  ^  <      Author:   CodCatDev
  ┌───────┐     License:  MIT
  │  CBX  │     Repo:     github.com/codcatdev/catbox
  └───────┘     Format:   .cbox (spec v1, magic: CBOX (43 42 4f 58))
                Codecs:   No
                Checksum: No
                Runtime:  {Host}
                OS:       {OsVersion}

""".lstrip('\n').rstrip()