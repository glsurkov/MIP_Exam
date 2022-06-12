def trapezoidVelocity(pos_0, pos_d, T, t ,v):
    a = (v ** 2) / (v * T - 1)
    diff = pos_d - pos_0

    if 0 <= t and t <= v/a:
        return (pos_0 + (a * (t ** 2) / 2) * diff, a * t * diff, a * diff)
    elif v/a < t and t <= (T - v/a):
        return (pos_0 + (v * t - (v ** 2) / (2 * a)) * diff, v * diff, 0)
    elif (T - v/a) < t and t <= T:
        return (
        pos_0 + ((2 * a * v * T - 2 * (v ** 2) - (a ** 2) * ((t - T) ** 2)) / (2 * a)) * diff, a * (T - t) * diff,
        -a * diff)
    else:
        return (pos_d, 0, 0)