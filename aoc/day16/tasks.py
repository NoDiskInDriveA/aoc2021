from __future__ import annotations
from enum import Enum
from functools import reduce
from typing import List
from dataclasses import dataclass


@dataclass
class BitReader:
    content: str
    pointer: int = 0

    def read_raw(self, n: int) -> str:
        old_pointer = self.pointer
        end_pointer = self.pointer + n
        self.pointer = end_pointer
        return self.content[old_pointer:end_pointer]

    def read_number(self, n: int) -> int:
        return int(self.read_raw(n), 2)

    def eof(self) -> bool:
        return self.pointer >= len(self.content)


class LengthType(Enum):
    TOTAL_BITS_LENGTH = 0
    SUB_PACKET_COUNT = 1


class PacketType(Enum):
    SUM = 0
    PRODUCT = 1
    MINIMUM = 2
    MAXIMUM = 3
    LITERAL = 4
    GREATER_THAN = 5
    LESS_THAN = 6
    EQUAL_TO = 7


@dataclass
class Packet:
    version: int
    packet_type: PacketType

    def version_sum(self) -> int:
        raise NotImplementedError

    def execute(self) -> int:
        raise NotImplementedError


@dataclass
class LiteralPacket(Packet):
    literal: int

    def version_sum(self) -> int:
        return self.version

    def execute(self) -> int:
        return self.literal


@dataclass
class OperatorPacket(Packet):
    length_type: LengthType
    subpackets: List[Packet] = None

    def append(self, packet: Packet) -> None:
        if self.subpackets is None:
            self.subpackets = []
        self.subpackets.append(packet)

    def version_sum(self) -> int:
        return self.version + sum((sub.version_sum() for sub in self.subpackets))

    def execute(self) -> int:
        sb_gen = (s.execute() for s in self.subpackets)

        if self.packet_type == PacketType.SUM:
            return sum(sb_gen)
        if self.packet_type == PacketType.PRODUCT:
            return reduce(lambda c, n: c * n, sb_gen, 1)
        if self.packet_type == PacketType.MAXIMUM:
            return max(sb_gen)
        if self.packet_type == PacketType.MINIMUM:
            return min(sb_gen)

        assert len(self.subpackets) == 2

        if self.packet_type == PacketType.GREATER_THAN:
            return int(self.subpackets[0].execute() > self.subpackets[1].execute())
        if self.packet_type == PacketType.LESS_THAN:
            return int(self.subpackets[0].execute() < self.subpackets[1].execute())
        if self.packet_type == PacketType.EQUAL_TO:
            return int(self.subpackets[0].execute() == self.subpackets[1].execute())

        raise ValueError('Cannot execute type %s' % (self.packet_type,))


def hex2bin_aligned(hexstr: str) -> str:
    return bin(int(hexstr, 16))[2:].zfill(len(hexstr) * 4)


def get_input() -> str:
    with open('input.txt', 'r') as fp:
        return hex2bin_aligned(fp.readline().strip())


def parse_literal_content(b: BitReader) -> int:
    value = ''
    while s := b.read_raw(5):
        value += s[1:]
        if s[0] == '0':
            break
    return int(value, 2)


def parse_next_packet(b: BitReader) -> Packet:
    version, packet_type = b.read_number(3), PacketType(b.read_number(3))
    if packet_type == PacketType.LITERAL:
        return LiteralPacket(version, packet_type, parse_literal_content(b))
    else:
        length_type = LengthType(b.read_number(1))
        p = OperatorPacket(version, packet_type, length_type)
        if length_type == LengthType.SUB_PACKET_COUNT:
            subpacket_count = b.read_number(11)
            while subpacket_count > 0:
                subpacket_count -= 1
                p.append(parse_next_packet(b))
        else:
            subpacket_length = b.read_number(15)
            subpacket_reader = BitReader(b.read_raw(subpacket_length))
            while not subpacket_reader.eof():
                p.append(parse_next_packet(subpacket_reader))

    return p


def parse_packets(b: BitReader):
    try:
        packet = parse_next_packet(b)
    except ValueError:
        if 'packet' in locals() and b.eof():
            print('End of stream')
            return packet
        raise

    return packet


def first_task():
    packet = parse_packets(BitReader(get_input()))
    print(packet.version_sum())


def second_task():
    packet = parse_packets(BitReader(get_input()))
    print(packet.execute())


def main():
    first_task()
    second_task()


if __name__ == '__main__':
    main()
