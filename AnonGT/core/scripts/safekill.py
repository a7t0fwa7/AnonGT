from core.config.functions import warn, exec_command, msg


def safekill():
    warn("killing dangerous processes & applications")
    # kill processes
    exec_command(
        "killall -q chrome dropbox skype icedove thunderbird firefox firefox-esr chromium xchat hexchat transmission steam firejail /usr/lib/firefox-esr/firefox-esr")
    # remove cache
    exec_command(
        "bleachbit -c adobe_reader.cache chromium.cache chromium.session chromium.history chromium.form_history elinks.history emesene.cache epiphany.cache firefox.cache firefox.crash_reports firefox.url_history firefox.forms flash.cache flash.cookies google_chrome.cache google_chrome.history google_chrome.form_history google_chrome.search_engines google_chrome.session google_earth.temporary_files links2.history opera.cache opera.form_history opera.history > /dev/null")

    msg("dangerous processes & applications killed")
