import math

def compare_methods(f, df, a, b, tol=1e-6, max_iter=100):
    """Compare steps for Bisection vs Newton-Raphson methods."""
    
    # Verify initial conditions
    if f(a) * f(b) >= 0:
        raise ValueError("Bisection needs f(a)*f(b) < 0")
    
    # Bisection method
    bisect_steps, a_, b_ = 0, a, b
    while bisect_steps < max_iter:
        c = (a_ + b_) / 2
        bisect_steps += 1
        if abs(f(c)) < tol or (b_ - a_)/2 < tol:
            break
        a_, b_ = (a_, c) if f(a_)*f(c) < 0 else (c, b_)
    
    # Newton-Raphson method
    newton_steps, x = 0, (a + b)/2
    while newton_steps < max_iter:
        fx = f(x)
        newton_steps += 1
        if abs(fx) < tol:
            break
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Zero derivative")
        x -= fx / dfx
    
    # Results
    faster = "Bisection" if bisect_steps < newton_steps else \
             "Newton-Raphson" if newton_steps < bisect_steps else \
             "Same steps"
    
    return {
        "bisection": bisect_steps,
        "newton": newton_steps,
        "faster": faster,
        "ratio": bisect_steps/newton_steps if newton_steps else math.inf
    }

# Example test
if __name__ == "__main__":
    f = lambda x: x**3 - 2*x - 5
    df = lambda x: 3*x**2 - 2
    res = compare_methods(f, df, 1, 3)
    print(f"Bisection: {res['bisection']} steps")
    print(f"Newton: {res['newton']} steps")
    print(f"Faster: {res['faster']}")
    print(f"Ratio: {res['ratio']:.1f}x")