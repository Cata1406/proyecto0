import { Box, List, ListItem } from "@mui/material";
import Task from "./Task";
import { useState } from "react";
import { get } from "http";

interface TaskListProps {
    setOpenPopUpEditTask: React.Dispatch<React.SetStateAction<boolean>>;
    setIsTaskUpdate: React.Dispatch<React.SetStateAction<boolean>>;
}

export interface TaskDetails {
    id: string;
    text: string;
    creation_date: string;
    forseen_end_date: string;
    state: string;
    user_id: string;
    category_id: string;
}

const TaskList = ({ setOpenPopUpEditTask, setIsTaskUpdate }: TaskListProps) => {
    const [tasks, setTasks] = useState<TaskDetails[]>([]); // This is the state that will store the tasks
    getTasksById(setTasks);
    return (
        <Box>
            <List>
                {tasks.map((task) => (
                    <ListItem>
                        <Task
                            setOpenPopUpEditTask={setOpenPopUpEditTask}
                            setIsTaskUpdate={setIsTaskUpdate}
                            task_details={task}
                        />
                    </ListItem>
                ))}
            </List>
        </Box>
    );
};

export default TaskList;

const getTasksById = async (
    setTasks: React.Dispatch<React.SetStateAction<TaskDetails[]>>
) => {
    const user_id = localStorage.getItem("user_id");
    const response = await fetch(
        `http://localhost:8000/users/${user_id}/tasks`,
        {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${localStorage.getItem("token")}`,
            },
        }
    );

    if (response.status === 200) {
        const data = await response.json();
        setTasks(data);
    } else {
        alert("Error obtaining tasks");
    }
};
