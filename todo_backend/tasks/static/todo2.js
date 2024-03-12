function addTask() {
    var input = document.getElementById("taskInput");
    var taskText = input.value;
    if (taskText.trim() !== "") {
        var taskList = document.getElementById("taskList");
        var taskDiv = document.createElement("div");
        taskDiv.classList.add("task");
        var taskTextDiv = document.createElement("div");
        taskTextDiv.classList.add("task-text");
        taskTextDiv.textContent = taskText;
        var taskActionsDiv = document.createElement("div");
        taskActionsDiv.classList.add("task-actions");
        var deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.onclick = function() {
            taskDiv.remove();
        };
        taskActionsDiv.appendChild(deleteButton);
        var checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.classList.add("task-checkbox");
        checkbox.onclick = function() {
            if (checkbox.checked) { 
                taskTextDiv.classList.add("completed");
                taskTextDiv.style.color = "green"; // Thêm màu xanh trực tiếp qua JS
                taskTextDiv.style.textDecoration = "line-through"; // Thêm gạch ngang trực tiếp qua JS
                taskTextDiv.style.textDecorationColor = "green"; // Đảm bảo màu của gạch ngang cũng là màu xanh
            } else {
                taskTextDiv.classList.remove("completed");
                taskTextDiv.style.color = ""; // Xóa style inline khi không hoàn thành
                taskTextDiv.style.textDecoration = "";
                taskTextDiv.style.textDecorationColor = "";
            }
        };
        taskDiv.appendChild(checkbox);
        taskDiv.appendChild(taskTextDiv);
        taskDiv.appendChild(taskActionsDiv);
        taskList.appendChild(taskDiv);
        input.value = "";
    } else {
        alert("Please enter a task!");
    }
}
