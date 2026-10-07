#!/usr/bin/env python3
"""Exact rational certificate for the spatial-coupling lower bound.

This verifies the scalar inequality in note.tex. The two
published probabilistic inputs are cited theorems, not verified by this code.
No floating point is used in any certificate decision.
"""

from fractions import Fraction as Q
import hashlib
import json


ALPHA = Q(3671741, 10**6)
ORDER = 128
TANGENCY_POINT = Q(883413964, 10**9)
MARGIN = Q(9, 10**8)


def horner(coefficients, x):
    value = Q(0)
    for coefficient in reversed(coefficients):
        value = value * x + coefficient
    return value


def certificate():
    if not __debug__:
        raise RuntimeError("Run without -O: the certificate requires assertion checks.")
    # P(t) = sum_{k=2}^N 4*t^(k-2)/(k*(k-1)) - alpha*t.
    coefficients = [Q(4, k * (k - 1)) for k in range(2, ORDER + 1)]
    coefficients[1] -= ALPHA
    derivative = [j * coefficients[j] for j in range(1, len(coefficients))]
    second_derivative = [j * derivative[j] for j in range(1, len(derivative))]

    assert 0 < TANGENCY_POINT < 1
    assert all(coefficient >= 0 for coefficient in second_derivative)
    assert second_derivative[0] > 0

    value = horner(coefficients, TANGENCY_POINT)
    slope = horner(derivative, TANGENCY_POINT)
    # An independent direct sum also checks the indexing in both polynomials.
    assert value == sum(
        Q(4, k * (k - 1)) * TANGENCY_POINT ** (k - 2)
        for k in range(2, ORDER + 1)
    ) - ALPHA * TANGENCY_POINT
    assert slope == sum(
        Q(4 * (k - 2), k * (k - 1)) * TANGENCY_POINT ** (k - 3)
        for k in range(3, ORDER + 1)
    ) - ALPHA

    # Convexity implies P(t) >= P(y)+P'(y)*(t-y) >= P(y)-abs(P'(y))
    # throughout [0,1]. These comparisons are exact integer comparisons.
    global_lower = value - abs(slope)
    assert value > Q(939, 10**10)
    assert abs(slope) < Q(4, 10**9)
    assert global_lower > MARGIN

    # This is a strict safety margin. For t in [0,1], increasing alpha by
    # MARGIN subtracts only MARGIN*t; positivity of P is preserved.
    exact_data = {
        "P_at_y": str(value),
        "P_prime_at_y": str(slope),
        "uniform_P_lower_bound": str(global_lower),
    }
    digest = hashlib.sha256(json.dumps(exact_data, sort_keys=True).encode()).hexdigest()
    return {
        "status": "PASS",
        "certified_lower_bound": str(ALPHA),
        "series_order": ORDER,
        "rational_tangency_point": str(TANGENCY_POINT),
        "strict_uniform_polynomial_margin": str(MARGIN),
        "checks_use_only_exact_rational_arithmetic": True,
        "proof_scope": "scalar potential inequality; cited probabilistic theorems are external inputs",
        "diagnostic_decimal_values_not_used_in_proof": {
            "P_at_y": float(value),
            "P_prime_at_y": float(slope),
            "uniform_P_lower_bound": float(global_lower),
        },
        "exact_values_sha256": digest,
        "exact_values": exact_data,
    }


if __name__ == "__main__":
    print(json.dumps(certificate(), indent=2))
