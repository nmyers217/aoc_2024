input = open("input.txt", "r").read().strip()


def build_drive():
    drive = []
    id = 0
    free = False
    for i in range(len(input)):
        n = int(input[i])
        for j in range(n):
            if free:
                drive.append(".")
            else:
                drive.append(str(id))
        id += 0 if free else 1
        free = not free
    return drive


def compact(drive):
    left, right = 0, len(drive) - 1

    while left < right:
        while drive[left] != "." and left < right:
            left += 1
        while drive[right] == "." and left < right:
            right -= 1
        if left < right:
            drive[left], drive[right] = drive[right], drive[left]

    return drive


def compact_files(drive):
    """I really don't care how ugly this is"""
    file_end = len(drive) - 1
    while file_end >= 0:
        while file_end >= 0 and drive[file_end] == ".":
            file_end -= 1
        file_start = file_end
        while file_start >= 0 and drive[file_start] == drive[file_end]:
            file_start -= 1
        sector_len = file_end - file_start
        if (
            drive[file_end] != "."
            and (start_index := find_sector(drive, sector_len)) is not None
            and start_index < file_start
        ):
            character = drive[file_end]
            for i in range(sector_len):
                drive[start_index + i] = character
                drive[file_start + 1 + i] = "."
        else:
            file_end = file_start
    return drive


def find_sector(drive, size):
    i = 0
    while i < len(drive):
        if drive[i] == ".":
            end = i
            while end < len(drive) and drive[end] == ".":
                end += 1
            sector_len = end - i
            if sector_len >= size:
                return i
            else:
                i = end
        else:
            i += 1


def checksum(drive):
    return sum(i * int(n) for i, n in enumerate(drive) if n != ".")


print(checksum(compact(build_drive())))
print(checksum(compact_files(build_drive())))
