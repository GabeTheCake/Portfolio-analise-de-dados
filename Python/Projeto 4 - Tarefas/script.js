// Selecionando elementos
const taskInput = document.getElementById('task-input');
const addButton = document.getElementById('add-btn');
const taskList = document.getElementById('task-list');

// Função para carregar tarefas salvas
function loadTasks() {
    const tasks = JSON.parse(localStorage.getItem('tasks')) || []; // Carregar tarefas ou array vazio
    taskList.innerHTML = ''; // Limpar a lista antes de recarregar

    if (tasks.length === 0) {
        const noTasksMessage = document.createElement('li');
        noTasksMessage.textContent = 'Nenhuma tarefa adicionada ainda.';
        taskList.appendChild(noTasksMessage);
    } else {
        tasks.forEach((task, index) => {
            const li = document.createElement('li');
            li.innerHTML = `
                <input type="checkbox" class="task-checkbox" ${task.completed ? 'checked' : ''}>
                <span class="task-text" style="text-decoration: ${task.completed ? 'line-through' : 'none'}">${task.text}</span>
                <button class="delete-btn">X</button>
            `;
            // Adicionar eventos de marcar como feito e excluir
            const checkbox = li.querySelector('.task-checkbox');
            checkbox.addEventListener('change', () => toggleTaskStatus(index));

            const deleteButton = li.querySelector('.delete-btn');
            deleteButton.addEventListener('click', () => deleteTask(index));

            taskList.appendChild(li);
        });
    }
}

// Função para adicionar tarefa
function addTask() {
    const taskText = taskInput.value.trim();
    
    if (taskText === "") {
        alert("Digite uma tarefa!");
        return;
    }

    const tasks = JSON.parse(localStorage.getItem('tasks')) || []; // Carregar tarefas ou array vazio
    tasks.push({ text: taskText, completed: false }); // Adicionar nova tarefa com status "não concluída"
    localStorage.setItem('tasks', JSON.stringify(tasks)); // Salvar no LocalStorage

    loadTasks(); // Recarregar tarefas
    taskInput.value = ''; // Limpar o campo de entrada
}

// Função para marcar tarefa como feita
function toggleTaskStatus(index) {
    const tasks = JSON.parse(localStorage.getItem('tasks')) || []; // Carregar tarefas
    tasks[index].completed = !tasks[index].completed; // Alternar o status da tarefa
    localStorage.setItem('tasks', JSON.stringify(tasks)); // Salvar no LocalStorage
    loadTasks(); // Recarregar tarefas
}

// Função para excluir tarefa
function deleteTask(index) {
    const tasks = JSON.parse(localStorage.getItem('tasks')) || []; // Carregar tarefas
    tasks.splice(index, 1); // Remover a tarefa pelo índice
    localStorage.setItem('tasks', JSON.stringify(tasks)); // Salvar no LocalStorage
    loadTasks(); // Recarregar tarefas
}

// Adicionar evento de clique no botão de adicionar
addButton.addEventListener('click', addTask);

// Adicionar tarefa pressionando Enter
taskInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        addTask();
    }
});

// Carregar tarefas ao iniciar a página
loadTasks();