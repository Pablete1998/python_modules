import sys
import importlib


def check_dependency(package_name: str) -> tuple[bool, str]:
    """Check if a package is installed and return its version."""
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, "__version__", "unknown")
        return True, version
    except ImportError:
        return False, "not installed"


def check_all_dependencies() -> dict[str, tuple[bool, str]]:
    """Check all required dependencies and return their status."""
    packages = ["pandas", "numpy", "matplotlib"]
    results: dict[str, tuple[bool, str]] = {}
    for package in packages:
        results[package] = check_dependency(package)
    return results


def show_dependency_status(results: dict[str, tuple[bool, str]]) -> bool:
    """Display dependency status and return True if all are available."""
    descriptions = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }

    print("Checking dependencies:")
    all_ok = True
    for package, (installed, version) in results.items():
        if installed:
            desc = descriptions.get(package, "Ready")
            print(f"  [OK] {package} ({version}) - {desc}")
        else:
            print(f"  [MISSING] {package} - not installed")
            all_ok = False

    if not all_ok:
        print()
        print("Some dependencies are missing!")
        print("Install them with pip:")
        print("  pip install -r requirements.txt")
        print()
        print("Or with Poetry:")
        print("  poetry install")

    return all_ok


def show_package_manager_comparison() -> None:
    """Show the differences between pip and Poetry."""
    print()
    print("Package manager comparison:")
    print()
    print("  pip:")
    print("    - Installs packages only")
    print("    - Uses requirements.txt")
    print("    - No automatic conflict resolution")
    print("    - Manual virtual environment management")
    print()
    print("  Poetry:")
    print("    - Installs packages + manages virtual environments")
    print("    - Uses pyproject.toml")
    print("    - Automatic dependency conflict resolution")
    print("    - Generates poetry.lock for reproducible installs")


def generate_matrix_data() -> "tuple[object, object]":  # type: ignore
    """Generate simulated Matrix data using numpy."""
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore

    np.random.seed(42)
    size = 1000

    timestamps = np.arange(size)
    signal_a = np.sin(timestamps * 0.1) + np.random.normal(0, 0.1, size)
    signal_b = np.cos(timestamps * 0.1) + np.random.normal(0, 0.1, size)
    anomalies = np.random.choice([0, 1], size=size, p=[0.95, 0.05])

    df = pd.DataFrame({
        "timestamp": timestamps,
        "signal_a": signal_a,
        "signal_b": signal_b,
        "anomaly": anomalies,
    })

    return df, np.array([signal_a, signal_b])


def analyze_data(df: "object") -> None:  # type: ignore
    """Analyze the Matrix data and print statistics."""
    print(f"  Processing {len(df)} data points...")  # type: ignore
    print(f"  Signal A - mean: {df['signal_a'].mean():.3f}, "  # type: ignore
          f"std: {df['signal_a'].std():.3f}")  # type: ignore
    print(f"  Signal B - mean: {df['signal_b'].mean():.3f}, "  # type: ignore
          f"std: {df['signal_b'].std():.3f}")  # type: ignore
    print(f"  Anomalies detected: {df['anomaly'].sum()}")  # type: ignore


def create_visualization(df: "object") -> None:  # type: ignore
    """Create and save a visualization of the Matrix data."""
    import matplotlib.pyplot as plt  # type: ignore

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))

    ax1.plot(df["timestamp"][:100], df["signal_a"][:100],  # type: ignore
             label="Signal A", color="green", alpha=0.8)
    ax1.plot(df["timestamp"][:100], df["signal_b"][:100],  # type: ignore
             label="Signal B", color="red", alpha=0.8)
    ax1.set_title("Matrix Signals")
    ax1.set_xlabel("Timestamp")
    ax1.set_ylabel("Amplitude")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    anomaly_data = df[df["anomaly"] == 1]  # type: ignore
    ax2.scatter(anomaly_data["timestamp"], anomaly_data["signal_a"],
                color="red", label="Anomalies", zorder=5)
    ax2.set_title("Anomaly Detection")
    ax2.set_xlabel("Timestamp")
    ax2.set_ylabel("Signal A")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    output_file = "matrix_analysis.png"
    plt.savefig(output_file)
    plt.close()
    print(f"  Results saved to: {output_file}")


def main() -> None:
    """Main entry point."""
    print("LOADING STATUS: Loading programs...")
    print()

    results = check_all_dependencies()
    all_ok = show_dependency_status(results)

    show_package_manager_comparison()

    if not all_ok:
        sys.exit(1)

    print()
    print("Analyzing Matrix data...")
    df, _ = generate_matrix_data()
    analyze_data(df)

    print("Generating visualization...")
    create_visualization(df)

    print()
    print("Analysis complete!")


if __name__ == "__main__":
    main()