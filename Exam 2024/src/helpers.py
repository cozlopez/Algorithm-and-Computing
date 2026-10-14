import matplotlib.pyplot as plt


def time_to_ms(time: str) -> int:
    minutes = int(time.split("'")[0])
    seconds_and_milliseconds = time.split("'")[1]
    seconds = int(seconds_and_milliseconds.split('"')[0])
    milliseconds = int(seconds_and_milliseconds.split('"')[1]) if '"' in seconds_and_milliseconds else 0
    return (minutes * 60 * 1000) + seconds * 1000 + milliseconds


def ms_to_time(time: int) -> str:
    minutes = time // 60000
    seconds = (time % 60000) // 1000
    milliseconds = seconds % 1000
    return f"{minutes}'{seconds}\"{milliseconds}"


def mu_vline(mu: float, y_min: float, y_max: float):
    plt.plot(
        [mu, mu],
        [y_min, y_max],
        color="tab:red",
        label=fr"$\mu = {mu}$",
    )


def sigma_vlines(mu: float, sigma: float, y_min: float, y_max: float):
    plt.plot(
        [mu - sigma, mu - sigma],
        [y_min, y_max],
        color="tab:orange",
        label=fr"$\sigma = {sigma}$",
    )
    plt.plot([mu + sigma, mu + sigma], [y_min, y_max], color="tab:orange")
