from prefect import flow

@flow(log_prints=True)
def run_script():
    x = 'abcd'
    print(x)
    return x
