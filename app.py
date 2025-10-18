tasks = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Ðã thêm công việc:'{task_name}'")
if __name__ == "__main__":
    print("Chào mừng bạn đến với To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
