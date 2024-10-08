import sys
import browser_cookie3


def main():
    """Print cookies."""
    cookiejar = None
    leetcode_com = "leetcode.com"

    try:
        cookiejar = browser_cookie3.chrome(domain_name=leetcode_com)
    except Exception:
        print("get cookie from Chrome failed", file=sys.stderr)

    # gain cookie from Chromium
    if not cookiejar:
        try:
            cookiejar = browser_cookie3.chromium(domain_name=leetcode_com)
        except Exception:
            print("get cookie from Chromium failed", file=sys.stderr)

    # gain cookie from Brave
    if not cookiejar:
        try:
            cookiejar = browser_cookie3.brave(domain_name=leetcode_com)
        except Exception:
            print("get cookie from Brave failed", file=sys.stderr)

    # gain cookie from Firefox
    if not cookiejar:
        try:
            cookiejar = browser_cookie3.firefox(domain_name=leetcode_com)
        except Exception:
            print("get cookie from Firefox failed", file=sys.stderr)

    # gain cookie from Safari
    if not cookiejar:
        try:
            cookiejar = browser_cookie3.safari(domain_name=leetcode_com)
        except Exception:
            print("get cookie from Safari failed", file=sys.stderr)

    # gain cookie from Microsoft Edge
    if not cookiejar:
        try:
            cookiejar = browser_cookie3.edge(domain_name=leetcode_com)
        except Exception:
            print("get cookie from Microsoft Edge failed", file=sys.stderr)
            return

    leetcode_cookies = list(
        filter(lambda c: c.name in ("LEETCODE_SESSION", "csrftoken"), cookiejar)
    )

    if len(leetcode_cookies) < 2:
        print(
            "get cookie failed, make sure you have Safari, Chrome, Chromium, Brave, Firefox or Edge installed and login in LeetCode with one of them at least once."
        )
        return

    for c in leetcode_cookies:
        print(c.name, c.value)


if __name__ == "__main__":
    main()
