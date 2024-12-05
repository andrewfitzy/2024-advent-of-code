# Standard Library
import math


class RuleSet:
    def __init__(self):
        self.must_appear_before = list()
        self.must_appear_after = list()


class Task02:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        # First need some way to store the rules
        rules, manuals = cls.build_rules_and_updates(file_content)

        # Process the manuals
        # if manual is incorrect add to to_be_printed
        to_be_printed = []
        for manual in manuals:
            if not cls.is_valid_update(manual, rules):
                fixed_manual = cls.get_fixed_manual(manual, rules)
                to_be_printed.append(fixed_manual)

        # Belt and braces check
        for manual in to_be_printed:
            if not cls.is_valid_update(manual, rules):
                print(f"THIS IS AN ISSUE 🚨🚨🚨🚨🚨🚨🚨🚨 ----> {manual}")

        # find middle page number, keep running total
        result = 0
        for manual in to_be_printed:
            middle_page = math.floor(len(manual) / 2)
            result = result + manual[middle_page]
        return result

    @classmethod
    def get_fixed_manual(cls, manual: list[int], rules: dict[int, RuleSet]) -> list[int]:
        # Sets help lookups
        manual_lookup = set(manual)

        # store the cut down version of the rules for this manual
        reduced_rules = {}

        # Strip out rules that we don't need and also take out page entries that don't appear in this manual
        for key, value in rules.items():
            if key in manual_lookup:
                page_ruleset = RuleSet()
                for page in value.must_appear_before:
                    if page in manual_lookup:
                        page_ruleset.must_appear_before.append(page)

                for page in value.must_appear_after:
                    if page in manual_lookup:
                        page_ruleset.must_appear_after.append(page)

                reduced_rules[key] = page_ruleset

        # The number of items that this entry needs to appear after gives its position in the list, for example the first entry appears after 0 other entries, the second entry appears after 1 other entry etc.
        result = [-1] * len(manual)
        for key, value in reduced_rules.items():
            result[len(value.must_appear_after)] = key
        return result

    @classmethod
    def build_rules_and_updates(cls, file_content: list[str]) -> tuple[dict[int, RuleSet], list[list[int]]]:
        rules: dict[int, RuleSet] = {}
        manuals: list[list[int]] = []
        rules_read = False
        for line in file_content:
            #  skip the empty line, this is then the start of the manual updates
            if len(line) == 0:
                rules_read = True
                continue

            # process the manual updates
            if rules_read:
                pages_txt = line.split(",")
                pages = [int(page) for page in pages_txt]
                manuals.append(pages)
                continue

            # build a dict of rules
            start, end = line.split("|")
            start_int = int(start)
            end_int = int(end)

            rule_set_start: RuleSet = rules.get(start_int, RuleSet())
            rule_set_start.must_appear_before.append(end_int)
            rules[start_int] = rule_set_start

            rule_set_end: RuleSet = rules.get(end_int, RuleSet())
            rule_set_end.must_appear_after.append(start_int)
            rules[end_int] = rule_set_end

        return (rules, manuals)

    @classmethod
    def is_valid_update(cls, manual: list[int], rules: dict[int, RuleSet]) -> bool:
        page_range = range(len(manual))
        for page in page_range:
            current_page = manual[page]

            remaining_pages = range(page + 1, len(manual))
            for next_page_index in remaining_pages:
                current_page_rules = rules[current_page]

                next_page = manual[next_page_index]
                next_page_rules = rules[next_page]

                if current_page in set(next_page_rules.must_appear_before) or next_page in set(
                    current_page_rules.must_appear_after
                ):
                    return False
        return True
