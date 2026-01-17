from app import metrics


def run_sample():
    return metrics.metrics_func_1('sample')

if __name__ == '__main__':
    print(run_sample())

