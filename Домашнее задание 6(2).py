def global_function():
    msg = 1
    def local_function():
        nonlocal msg
        msg = 2
        return print(msg)
    local_function()
global_function()



