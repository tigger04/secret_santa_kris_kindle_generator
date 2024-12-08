#!/usr/bin/env python3
import sys
import random


def parse_input():
    candidates = set()
    constraints = (
        []
    )  # Each element is a list of candidates that can't be paired together

    # Read all lines from STDIN
    input_data = sys.stdin.read().strip()
    for line in input_data.split("\n"):
        line = line.strip()
        if not line:
            continue
        # Remove comments: everything after '#'
        if "#" in line:
            line = line[: line.index("#")].strip()
        if not line:
            continue

        tokens = [t.strip() for t in line.split() if t.strip()]
        if tokens:
            # Add to candidates
            candidates.update(tokens)
            # Add this group to constraints
            constraints.append(tokens)

    return list(candidates), constraints


def check_constraints(matched_pairs, constraints):
    # matched_pairs is a list of tuples (a, b)
    # constraints is a list of lists [c1, c2, c3, ...]
    for pair in matched_pairs:
        a, b = pair
        # Check each constraint group
        for group in constraints:
            # If both a and b are in the same group, this violates constraints
            if a in group and b in group:
                return False
            if a == b:
                return False
    # print(f"Constraints met: {matched_pairs}")
    return True


def attempt_allocation(candidates, constraints, max_attempts=10000):
    """
    Attempt to allocate candidates into random pairs.

    candidates: list of candidate names
    constraints: list of lists, each sub-list containing candidates that cannot appear together

    Returns:
        A list of (giver, receiver) pairs, and if odd number of candidates,
        the last one is (candidate, None).
    """
    n = len(candidates)
    if n == 0:
        return []

    # Create a copy of candidates to shuffle
    candidates_copy = candidates.copy()
    # Shuffle candidates to get a random allocation
    random.shuffle(candidates_copy)

    # Create random pairs
    matched_pairs = []
    available_receivers = candidates_copy.copy()

    for giver in candidates_copy:
        # if giver in available_receivers:
        #     available_receivers.remove(giver)  # Can't give to self

        # debug giver
        # print(f"Attempting to match {giver}...")

        if available_receivers:
            receiver = random.choice(available_receivers)
            pair = [giver, receiver]
            # print(f"  Picked {receiver}")
            # if check_constraints([pair], constraints):
            matched_pairs.append((giver, receiver))
            available_receivers.remove(receiver)
            # else:
            #     print(f"  Constraint violated, scratch that ...")
        else:
            # No available receivers left, warn:
            # print(f"Warning: No available receivers left for {giver}.")
            matched_pairs.append((giver, None))

    return matched_pairs
    # Check if this allocation meets the constraints
    # if check_constraints(matched_pairs, constraints):
    #     return matched_pairs

    # raise ValueError("Could not find valid allocation.")


def main():
    candidates, constraints = parse_input()
    print("Number of candidates:", len(candidates))
    print("Candidates:", candidates)
    print("Constraints (no two from the same line can pair):", constraints)

    max_total_attempts = 99999
    attempt = 0

    while attempt < max_total_attempts:
        try:

            # print(f"iteration: {attempt}")
            
            matches = attempt_allocation(candidates, constraints)

            # Check if there are any unmatched candidates
            has_unmatched = any(match[1] is None for match in matches)

            if check_constraints(matches, constraints):
                # Success! We found a valid allocation with constraints met
                print("\nGenerated Matches:")
                for g, r in matches:
                    print(f"{g} → {r}")
                break

            # If we have unmatched candidates, continue to next attempt
            attempt += 1

        except ValueError:
            # If allocation failed, try again
            attempt += 1
            continue

    if attempt >= max_total_attempts:
        print(f"Error: No valid allocation found after {max_total_attempts} attempts.")

    print(f"After {attempt} iterations")


if __name__ == "__main__":
    main()
