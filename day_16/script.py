#!/usr/bin/env python3


def get_inputs(filename: str) -> int:
    with open(filename) as fp:
        data = fp.read().splitlines()
        fp.close()

    res = []
    for b in bytearray.fromhex(data[0]):
        for i in range(8):
            res.append((b >> (7 - i)) & 1)
    return res


def to_int(bits: [int]) -> int:
    res = 0
    for b in bits:
        res = res << 1 | b
    return res


def solve(data: [int]):
    values, version, i = [], 0, 0
    if not data:
        return values, version, i

    packet_version = to_int(data[i : i + 3])
    version += packet_version
    i += 3

    packet_type = to_int(data[i : i + 3])
    i += 3

    if packet_type == 4:
        literal_value = 0
        while True:
            v = to_int(data[i : i + 5])
            i += 5
            literal_value = (literal_value << 4) | (v & 15)
            if not (v & 16):
                break
        values += [literal_value]
    else:
        length_type_id = to_int(data[i : i + 1])
        i += 1
        if length_type_id == 0:
            subpackets_bits = to_int(data[i : i + 15])
            i += 15
            dst = i + subpackets_bits
            while i < dst:
                val, ver, ii = solve(data[i:])
                values += val
                version += ver
                i += ii
        else:
            num_subpackets = to_int(data[i : i + 11])
            i += 11
            for _ in range(num_subpackets):
                val, ver, ii = solve(data[i:])
                values += val
                version += ver
                i += ii

        if packet_type == 0:
            values = [sum(values)]
        elif packet_type == 1:
            n = 1
            for v in values:
                n *= v
            values = [n]
        elif packet_type == 2:
            values = [min(values)]
        elif packet_type == 3:
            values = [max(values)]
        elif packet_type == 5:
            values = [1] if values[0] > values[1] else [0]
        elif packet_type == 6:
            values = [1] if values[0] < values[1] else [0]
        elif packet_type == 7:
            values = [1] if values[0] == values[1] else [0]
    return values, version, i


p2, p1, _ = solve(get_inputs("input.txt"))
print("part 1:", p1)
print("part 2:", p2[0])
