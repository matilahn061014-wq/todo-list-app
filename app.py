# Danh sách d? luu các công vi?c
tasks = []

def add_task(task_name):
    """Thêm m?t công vi?c m?i vào danh sách."""
    tasks.append(task_name)
    print(f"Ðã thêm công vi?c: '{task_name}'")

# --- Ði?m b?t d?u c?a chuong trình ---
if __name__ == "__main__":
    print("Chào m?ng d?n v?i ?ng d?ng To-Do List!")
    add_task("H?c bài Git và GitHub")
    add_task("Làm bài t?p th?c hành ? nhà")