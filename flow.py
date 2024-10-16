from prefect import flow

@flow(log_prints=True)
def my_flow():
    print("I'm a flow from a GitHub repo! And I've changed!")
