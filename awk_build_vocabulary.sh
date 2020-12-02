#!/usr/bin/awk -f
# print all the commands from a mapping rule

BEGIN {
    in_mapping = 0
}

/^    mapping\s*=\s*{/{
    in_mapping = 1
    # print("in mapping")
}

/^        "/ {
    if (in_mapping) {
        # print($0)
        # match(string, regexp [, array])
        # substr(string, start [, length ])
        start = match($0, /"/)
        end = match($0, /":/)
        # print(start)
        # print(end)
        command = substr($0, start + 1, end - start - 1)
        print(command)
    }
}

/}/ {
    if (in_mapping) {
        in_mapping = 0
    }
}
