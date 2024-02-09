import { Button } from "@mui/material";
import { useState } from "react";
import PlusIcon from "@mui/icons-material/Add";
import TaskList from "../components/TaskList";
import PopUpEditTask from "../components/PopUpEditTask";

const TasksPage = () => {
    const [openPopUpEditTask, setOpenPopUpEditTask] = useState(false);
    const [isTaskUpdate, setIsTaskUpdate] = useState(true);

    const handleClose = () => {
        setOpenPopUpEditTask(false);
    };

    return (
        <div>
            <Button
                variant="text"
                startIcon={<PlusIcon />}
                onClick={() => {
                    setIsTaskUpdate(false); // If not an update, the task is new
                    setOpenPopUpEditTask(true);
                }}
            >
                Add task
            </Button>
            <PopUpEditTask
                openPopUpEditTask={openPopUpEditTask}
                setOpenPopUpEditTask={setOpenPopUpEditTask}
                handleClose={handleClose}
                isUpdate={isTaskUpdate}
                setIsTaskUpdate={setIsTaskUpdate}
            />
            <TaskList
                setOpenPopUpEditTask={setOpenPopUpEditTask}
                setIsTaskUpdate={setIsTaskUpdate}
            />
        </div>
    );
};

export default TasksPage;
