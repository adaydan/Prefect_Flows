from prefect import flow

@flow(log_prints=True)
def my_flow():
    print("I've made my own repo now :)")
