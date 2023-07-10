def generate_count():
    container = [0]

    def add_one():
        container [0] += 1
        print(f"当前是第{container[0]}次调用")

    return add_one

result = generate_count()

result()
result()
result()
result()
