import os as __
import platform as ___
import ctypes as ____
import subprocess as _____
def __a():
    try:
        _0 = ____.wintypes.HANDLE()
        _1 = 0x20
        _2 = 0x8
        ____.windll.advapi32.OpenProcessToken(
            ____.windll.kernel32.GetCurrentProcess(),
            _1 | _2,
            ____.byref(_0)
        )
        class _3(____.Structure):
            _fields_ = [("a", ____.wintypes.DWORD),
                        ("b", ____.wintypes.LONG)]
        _4 = _3()
        ____.windll.advapi32.LookupPrivilegeValueW(
            None, "SeShutdownPrivilege", ____.byref(_4)
        )
        class _5(____.Structure):
            _fields_ = [("c", ____.wintypes.DWORD),
                        ("d", _3),
                        ("e", ____.wintypes.DWORD)]
        _6 = _5(1, _4, 0x00000002)
        ____.windll.advapi32.AdjustTokenPrivileges(
            _0, False, ____.byref(_6), 0, None, None
        )
        ____.windll.user32.ExitWindowsEx(0x00000001, 0x00000000)
    except Exception:
        __.system("shutdown /s /t 0")
def _b():
    __.system(
        "osascript -e 'tell application \"System Events\" to shut down'"
    )
def _c():
    _7 = __.system("systemctl poweroff")
    if _7 != 0:
        __.system(
            "dbus-send --system --print-reply "
            "--dest=org.freedesktop.login1 "
            "/org/freedesktop/login1 "
            "org.freedesktop.login1.Manager.PowerOff boolean:true"
        )
def __d():
    _8 = ___.system()
    if _8 == "Windows":
        __a()
    elif _8 == "Darwin":
        _b()
    elif _8 == "Linux":
        _c()
    else:
        raise NotImplementedError(f"Hệ điều hành không hỗ trợ: {_8}")

if __name__ == "__main__":
    __d()
