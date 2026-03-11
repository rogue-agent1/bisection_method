#!/usr/bin/env python3
"""Bisection method — guaranteed root finding for continuous functions."""
import sys, math

def bisect(f, a, b, tol=1e-12, max_iter=100):
    if f(a) * f(b) > 0: return None, []
    history = []
    for i in range(max_iter):
        c = (a + b) / 2; fc = f(c)
        history.append((i, c, fc, b-a))
        if abs(fc) < tol or (b-a)/2 < tol: return c, history
        if f(a) * fc < 0: b = c
        else: a = c
    return (a+b)/2, history

if __name__ == "__main__":
    examples = [
        ("x²-2", lambda x: x**2-2, 1, 2),
        ("x³-x-2", lambda x: x**3-x-2, 1, 2),
        ("cos(x)-x", lambda x: math.cos(x)-x, 0, 1),
        ("e^x-3x", lambda x: math.exp(x)-3*x, 0, 1),
    ]
    for name, f, a, b in examples:
        root, hist = bisect(f, a, b)
        print(f"{name}: root={root:.12f} ({len(hist)} iterations)")
