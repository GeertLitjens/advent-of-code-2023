"""
"""
import re

from advent_of_code_2023.utils import Solution


class DaySolution(Solution):
    def __init__(self: "DaySolution", day: int = 5, year: int = 2023) -> None:
        super().__init__(day, year)

    def _parse_data(
        self: "DaySolution", input_data: str
    ) -> tuple[list[int], list[list[tuple[range, range]]]]:
        """ """
        unparsed_seeds, *unparsed_maps = input_data.split("\n\n")
        seeds = [int(x) for x in re.findall(r"\d+", unparsed_seeds)]
        seed_maps: list[list[tuple[range, range]]] = []
        for i, map in enumerate(unparsed_maps):
            seed_maps.append([])
            _, *triplets = map.splitlines()
            for triplet in triplets:
                dest, src, rng = [int(x) for x in re.findall(r"\d+", triplet)]
                seed_maps[i].append((range(src, src + rng), range(dest, dest + rng)))
        return (seeds, seed_maps)

    def _solve_part1(
        self: "DaySolution",
        parsed_data: tuple[list[int], list[list[tuple[range, range]]]],
    ) -> str:
        """ """
        seeds, seed_maps = parsed_data
        mapped_locations = []
        for seed in seeds:
            cur_nr = seed
            for map in seed_maps:
                for rule in map:
                    if cur_nr in rule[0]:
                        cur_nr = rule[1].start + (cur_nr - rule[0].start)
                        break
            mapped_locations.append(cur_nr)
        return str(min(mapped_locations))

    def _solve_part2(
        self: "DaySolution",
        parsed_data: tuple[list[int], list[list[tuple[range, range]]]],
    ) -> str:
        """ """
        seed_data, seed_maps = parsed_data
        result_ranges = [
            range(seed_data[i], seed_data[i] + seed_data[i + 1])
            for i in range(0, len(seed_data), 2)
        ]
        for map in seed_maps:
            current_ranges = result_ranges
            result_ranges = []
            while current_ranges:
                remainder = current_ranges.pop()
                intersected = False
                for rule in map:
                    intersect = range(
                        max(rule[0].start, remainder.start),
                        min(rule[0].stop, remainder.stop),
                    )
                    if len(intersect) > 0:
                        intersected = True
                        result_ranges.append(
                            range(
                                rule[1].start + intersect.start - rule[0].start,
                                rule[1].start + intersect.stop - rule[0].start,
                            )
                        )
                        if rule[0].start > remainder.start:
                            current_ranges.append(range(remainder.start, rule[0].start))
                        if rule[0].stop < remainder.stop:
                            current_ranges.append(range(rule[0].stop, remainder.stop))
                        break
                if not intersected:
                    result_ranges.append(remainder)
        return str(min([x.start for x in result_ranges]))
